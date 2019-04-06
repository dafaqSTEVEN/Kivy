import os
import time
import datetime
from time import strftime
from datetime import timedelta
starting_time = time.time()
trip_route_convertion = []
ending_time = starting_time + 20
dir_path = os.path.dirname(os.path.realpath(__file__))
print('\rLoading data...')
exec (open(dir_path + '\\agency.py').read())
exec (open(dir_path + '\\fare_attributes.py').read())
exec (open(dir_path + '\\fare_rules.py').read())
exec (open(dir_path + '\\frequencies.py').read())
exec (open(dir_path + '\\route.py').read())
exec (open(dir_path + '\\stop.py').read())
exec (open(dir_path + '\\trips.py').read())
exec (open(dir_path + '\\stop_time.py').read())

print("Time usage : " + str(round(time.time() - starting_time, 3)) + ' seconds.\n')

a = input('Route name ? ')

n = 1
temp = []
list_time_id = []
try:
    temp.append(route_dict[a])
    while True:
        if route_dict.get(str(a + '_' + str(n))) is None:
            break
        else:
            temp.append(route_dict[str(a + '_' + str(n))])
            n += 1
except KeyError:
    print('No such route')

print('Search Result:\n-------------------------------------------')

for i in range(len(temp)):
    global zz1
    if int(temp[i][4]) == 0:
        zz1 = 'Tram'
    elif int(temp[i][4]) == 1:
        zz1 = 'Subway'
    elif int(temp[i][4]) == 2:
        zz1 = 'Rail'
    elif int(temp[i][4]) == 3:
        zz1 = 'Bus'
    elif int(temp[i][4]) == 4:
        zz1 = 'Ferry'
    elif int(temp[i][4]) == 5:
        zz1 = 'Cable Tram'
    elif int(temp[i][4]) == 6:
        zz1 = 'Aerial Lift'
    elif int(temp[i][4]) == 7:
        zz1 = 'Funicular'
    e = temp[i]
    print('Route ID : ' + str(e[0]) + '\nAgency ID : ' + str(e[1]) + '\nRoute name : ' + str(
        e[2]) + '\nRoute Full name : ' + str(e[3]) + '\nRoute type : ' + str(zz1) + '\nRoute URL : ' + str(
        e[5]) + '\n-------------------------------------------\n')



b = 0

def b_func():
    if len(temp) > 1:
        global b
        b = int(input('Which?\n'))

b_func()

for key in trip.keys():
    if b == 0:
        if temp[b][0] in trip[key]:
            trip_route_convertion.append(key)
    elif temp[b-1][0] in trip[key]:
        trip_route_convertion.append(key)


for i in range(len(trip_route_convertion)):
    list_time_id.append(trip_route_convertion[i].split('-')[3])
time_dict = {}
time_list = []
print ('The time now is: ' +strftime('%H%M'))
for i in range(len(list_time_id)):
    t1 =timedelta(hours =int(strftime('%H')),minutes = int(strftime('%M')))
    t2 =timedelta(hours =int(list_time_id[i][0] +list_time_id[i][1]), minutes =int(list_time_id[i][2]+list_time_id[i][3]))
    t3 =t2 -t1
    if t3 < timedelta(0):
        pass
    else:
        time_list.append(t3)
        time_dict[str(t2)] = str(t3)

t4 = min(time_list)
for key in time_dict.keys():
    if str(t4) in time_dict[key]:
        print('The next bus will arrive at : ' + key)
        break
    break

trip_1 = []
for i in range(len(trip_route_convertion)):
    for key in stop_time:
        if trip_route_convertion[i] == stop_time[key][0]:
            if [stop_time[key][3],stop_time[key][4]] not in trip_1:
                trip_1.append([stop_time[key][3],stop_time[key][4]])

for i in range(len(trip_1)):
    print('>The stop Name is '+str(stop[trip_1[i][0]][1]) +' (Stop ID:'+str(trip_1[i][0])+')'+'\n>'+'The Stop Sequence is ' + str(trip_1[i][1]+'\n'))
    print('--------------------------------------------------')








