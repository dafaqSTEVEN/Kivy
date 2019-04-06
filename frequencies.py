import csv
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

frequency = {}
trip_id = []
start_time = []
end_time = []
headway_secs = []

with open(dir_path + '\\bus_en\\frequencies.csv') as d:
    frequecies_data = csv.DictReader(d,delimiter = ',')
    for row in frequecies_data:
        trip_id.append(row['trip_id'])
        start_time.append(row['start_time'])
        end_time.append(['end_time'])
        headway_secs.append(['headway_secs'])

for i in range(len(trip_id)):
    frequency[trip_id[i]] = [trip_id[i],start_time[i],end_time[i],headway_secs[i]]