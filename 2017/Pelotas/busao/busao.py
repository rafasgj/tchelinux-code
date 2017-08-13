from kdtree import KDTree
from gps import haversine_distance, haversine_manhattan
from gtfs import read_gtfs_stoptimes, read_gtfs_file, Route, Stop, StopTimes
from math import ceil

routes = read_gtfs_file('gtfs/routes.txt',Route)
stops = read_gtfs_file('gtfs/stops.txt',Stop)
stop_times = read_gtfs_stoptimes('gtfs/stop_times.txt')

# HOME: -30.010644, -51.202583
# SENAC: -30.035195, -51.226591
# MERCADO PUBLICO: -30.026952, -51.227694
# MERCADO PUBLICO 2: -30.027621, -51.227297
# AEROPORTO: -29.989756, -51.177452
# PUCRS: -30.057356, -51.174642

stops_tree = KDTree(stops)

origin = [ float(x) for x in input("\nOrigin (lat, lon): ").split(",")]
o_stops=stops_tree.getClosestPoints(origin,count=15,distance=haversine_distance)

dest= [ float(x) for x in input("\nDestination (lat, lon): ").split(",")]
d_stops=stops_tree.getClosestPoints(dest,count=15,distance=haversine_distance)

def filter_stops():
    visited = set([])
    for stop, dist in d_stops:
        try:
            if stop.stop_id in visited: continue
            for route in stop_times[stop.stop_id].keys():
                if route in visited: continue
                visited.add(route)
                for origin, origin_dist in o_stops:
                    if route in stop_times[origin.stop_id]:
                        for r in routes:
                            if r.route_id == route:
                                print ("\n\nONIBUS: (%s) %s" % \
                                        (route, r.route_long_name))
                        print ("ORIGEM: ",origin.stop_name)
                        print ("DESTINO:",stop.stop_name)
                        d = ceil(dist+origin_dist)
                        print ("Total de Caminhada: %dm"%d)
                        break
        except:
            print ("Rota nao encontrada:",stop.stop_id)

filter_stops()
