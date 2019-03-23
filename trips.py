import csv

trip = {}
route_id = []
service_id = []
trip_id = []
with open("E:\\Program\\GITHUBKIVY\\MY\\Kivy\\bus_en\\trips.csv",'rt',encoding = 'utf8') as f:
    trip_dict = csv.DictReader(f ,delimiter=',')
    for row in trip_dict:
        route_id.append(row['route_id'])
        service_id.append(row['service_id'])
        trip_id.append(row['trip_id'])

for i in range(len(route_id)):
    trip[str(trip_id[i])] = [route_id[i],service_id[i],trip_id[i]]

print(trip)