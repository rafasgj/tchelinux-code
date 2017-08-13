
from math import cos, sin, sqrt, atan2, radians

def haversine_distance(gps_a, gps_b):
    R = 6371000.8
    lat_a, lon_a = gps_a[:2]
    lat_b, lon_b = gps_b[:2]
    dlat = radians(lat_a - lat_b)
    dlon = radians(lon_a - lon_b)
    coslat = cos(radians(lat_a))
    cosother = cos(radians(lat_b))

    a = sin(dlat/2)**2 + coslat * cosother * (sin(dlon/2) ** 2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    
    return R * c

def haversine_manhattan(gps_a, gps_b):
    gps_c = (gps_a[0],gps_b[1])
    ha = haversine_distance(gps_a, gps_c)
    hb = haversine_distance(gps_b, gps_c)
    return ha + hb

