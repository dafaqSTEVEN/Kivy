import quandl
from datetime import date,timedelta
import datetime

# try:
quandl.ApiConfig.api_key = 'KVPSsy7GuZrgRNx9Gxhd'
c = input('How many days ago :')
a = input('Stock ID: ')
b = quandl.get('HKEX/' + a , start_date= datetime.date.today() - datetime.timedelta(days = int(c)), end_date=date.today())
print(b)
# except:
#     print('Error')
