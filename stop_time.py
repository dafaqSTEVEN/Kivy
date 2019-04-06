import csv
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

stop_time = {}
trip_id = []
arrival_time = []
departure_time = []
stop_id = []
stop_sequence = []
pickup_type = []
drop_off_type = []
timepoint = []

with open(str(dir_path + "\\bus_en\\stop_times.csv")) as s:
    datas = csv.DictReader(s, delimiter = ',')
    for row in datas:
        trip_id.append(row['trip_id'])
        arrival_time.append(row['arrival_time'])
        departure_time.append(row['departure_time'])
        stop_id.append(row['stop_id'])
        stop_sequence.append(row['stop_sequence'])
        pickup_type.append(row['pickup_type'])
        drop_off_type.append(row['drop_off_type'])
        timepoint.append(row['timepoint'])

'''
print(arrival_time)
if arrival_time[1] == str(''):
    print('NONE')
'''
for i in range(len(trip_id)):
    stop_time[i] = [trip_id[i],arrival_time[i],departure_time[i],stop_id[i],stop_sequence[i],pickup_type[i],drop_off_type[i],timepoint[i]]
'''
print (stop_time)
'''
