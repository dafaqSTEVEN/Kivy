import csv
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
stop = {}

stop_id = []
stop_name = []
stop_lat = []
stop_lon = []
zone_id = []
location_type = []
stop_timezone = []

with open(str(dir_path + "\\bus_en\\stops.csv"),'rt',encoding = 'utf8') as f:
    stop_dict = csv.DictReader(f ,delimiter=',')
    for row in stop_dict:
        stop_id.append(row['stop_id'])
        stop_name.append(row['stop_name'])
        stop_lat.append(row['stop_lat'])
        stop_lon.append(row['stop_lon'])
        location_type.append(row['location_type'])
        stop_timezone.append(row['stop_timezone'])

for i in range(len(stop_id)):
    stop[str(stop_id[i])] = [stop_id[i],stop_name[i],stop_lat[i],stop_lon[i],location_type[i],stop_timezone[i]]

'''
print(stop)
'''