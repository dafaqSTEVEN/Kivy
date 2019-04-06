import csv
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

fare = {}
fare_id = []
route_id = []
origin_id = []
destination = []

with open(dir_path + '\\bus_en\\fare_rules.csv') as q:
    fare_data = csv.DictReader(q,delimiter = ',')
    for row in fare_data:
        fare_id.append(row['fare_id'])
        route_id.append(row['route_id'])
        origin_id.append(row['origin_id'])
        destination.append(row['destination_id'])

for i in range(len(fare_id)):
    fare[fare_id[i]] = [fare_id[i],route_id[i],origin_id[i],destination[i]]
