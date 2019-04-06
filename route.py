import csv
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

route_dict = {}

route_id = []
agency_id = []
route_short_name = []
route_long_name = []
route_type = []
route_url = []

with open(str(dir_path + "\\bus_en\\routes.csv")) as q:
    route_data = csv.DictReader(q, delimiter=',')
    for row in route_data:
        temp_route_id = row['route_id']
        route_id.append(temp_route_id)
        temp_agency_id = row['agency_id']
        agency_id.append(temp_agency_id)
        temp_route_short_name = row['route_short_name']
        route_short_name.append(temp_route_short_name)
        temp_route_long_name = row['route_long_name']
        route_long_name.append(temp_route_long_name)
        temp_route_type = row['route_type']
        route_type.append(temp_route_type)
        temp_route_url = row['route_url']
        route_url.append(temp_route_url)


for i in range(len(route_short_name)):
    if route_dict.get(route_short_name[i]) is None:
        route_dict[str(route_short_name[i])] = [route_id[i], agency_id[i], route_short_name[i], route_long_name[i],route_type[i], route_url[i]]
    else:
        for g in range(15):
            if (route_dict.get(route_short_name[i]) is not None) and route_dict.get(str(route_short_name[i]) + ('_' + str(g+1))) is None:
                route_dict[str(route_short_name[i]+'_'+str(g+1))] = [route_id[i], agency_id[i], route_short_name[i], route_long_name[i],route_type[i], route_url[i]]
                break


'''

h = input('Tell me the short_name: ')
j = input('Tell me the info : ')
global x
if j == 'route_id':
    x = 0
elif j == 'agency_id':
    x = 1
elif j == 'route_short_name':
    x = 2
elif j == 'route_long_name':
    x = 3
elif j == 'route_type':
    x = 4
elif j == 'route_url':
    x = 5

temp = []

n = 1
try:
    temp.append(str(route_dict[h][x]))
    while True:
            if route_dict.get(str(h + '_' + str(n))) is None:
                break
            else:
                temp.append(route_dict[str(h + '_' + str(n))][x])
                n += 1
except KeyError:
    print('No such route')


print (temp)



for i in range(len(temp)):
    print('The ' + str(j) + ' is ' + str(temp[i]))
'''
