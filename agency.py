import csv

agency = {}

agency_id = []
agency_name = []
agency_url = []
agency_timezone = []
agency_lang = []
agency_phone = []
agency_email = []


with open("E:\\Program\\GITHUBKIVY\\MY\\Kivy\\bus_en\\agency.csv") as f:
    data = csv.DictReader(f, delimiter=',')
    for row in data:
        temp_agency_id = row['agency_id']
        agency_id.append(temp_agency_id)
        temp_agency_name = row['agency_name']
        agency_name.append(temp_agency_name)
        temp_agency_url = row['agency_url']
        agency_url.append(temp_agency_url)
        temp_agency_timezone = row['agency_timezone']
        agency_timezone.append(temp_agency_timezone)
        temp_agency_lang = row['agency_lang']
        agency_lang.append(temp_agency_lang)
        temp_agency_phone = row['agency_phone']
        agency_phone.append(temp_agency_phone)
        temp_agency_email = row['agency_email']
        agency_email.append(temp_agency_email)

'''
print(agency_id)
print('------------------------------------------')
print(agency_name)
print('------------------------------------------')
print(agency_url)
print('------------------------------------------')
print(agency_timezone)
print('------------------------------------------')
print(agency_lang)
print('------------------------------------------')
print(agency_phone)
print('------------------------------------------')
print(agency_email)
'''

for i in range(len(agency_id)):
    agency[str(agency_id[i])] = [agency_id[i],agency_name[i],agency_url[i],agency_timezone[i],agency_lang[i],agency_phone[i],agency_email[i]]

'''
while True:
    h = input('Tell me the Agency ID : ')
    j = input('Tell me the info : ')
    if j =='agency_id':
        x = 0
    elif j =='agency_name':
        x = 1
    elif j =='agency_url':
        x = 2
    elif j =='agency_timezone':
        x = 3
    elif j == 'agency_lang':
        x = 4
    elif j == 'agency_phone':
        x = 5
    elif j == 'agency_email':
        x = 6

    temp = agency[h.upper()]
    print('The ' + str(j)+ ' is '+temp[x])
    x = 0
    break
'''


