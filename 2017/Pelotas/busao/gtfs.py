from collections import namedtuple
import csv

class Route(namedtuple('Route','route_id route_long_name')):
    def __repr__(self):
        return ('%s:%s') % (self.route_id,self.route_long_name)

class Trip(namedtuple('Trip','route_id trip_id')):
    def __repr__(self):
        return ('%s:%s') % (self.route_id,self.trip_id)

class StopTimes(namedtuple('Trip','stop_id trip_id stop_sequence')):
    def __repr__(self):
        return ('%s:%s,%s') % (self.stop_id,self.trip_id,self.stop_sequence)

class Stop(namedtuple('Stop','stop_lat stop_lon stop_id stop_name')):
    def __new__(cls, lat, lon, sid, name):
        lat = float(lat)
        lon = float(lon)
        return super(cls, Stop).__new__(cls, lat, lon, sid, name.strip())

    def __repr__(self):
        return ('%s:(%s,%s),%s') % \
                (self.stop_name,self.stop_lat,self.stop_lon,self.stop_id)

    def __len__(self):
        return 2

def read_gtfs_file(filename, cls):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        return [cls(*args) for args in
                [tuple([row[k] for k in cls._fields]) for row in reader]]

def read_gtfs_stoptimes(filename):
    output = {}
    with open(filename) as csvfile:
        for row in csv.reader(csvfile):
            trip_id, *_, stop_id, stop_sequence = row
            if trip_id == 'trip_id': continue # ignore first line
            route_id = trip_id.split('-')[0]
            output.setdefault(stop_id, {})[route_id] = int(stop_sequence);
    return output

