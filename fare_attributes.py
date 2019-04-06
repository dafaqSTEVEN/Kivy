import csv
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

fare_attributes = {}
fare_id = []
price = []
currency_type = []
payment_method = []
transfers = []
agency_id = []

with open(dir_path + '\\bus_en\\fare_attributes.csv') as t:
    fare_dataset = csv.DictReader( t ,delimiter = ',')
    for row in fare_dataset:
        fare_id.append(row['fare_id'])
        price.append(row['price'])
        currency_type.append(row['currency_type'])
        payment_method.append(row['payment_method'])
        transfers.append(row['transfers'])
        agency_id.append(row['agency_id'])

for i in range(len(fare_id)):
    fare_attributes[fare_id[i]] = [fare_id[i],price[i],currency_type[i],payment_method[i],transfers[i],agency_id[i]]