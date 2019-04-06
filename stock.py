import quandl
from datetime import date,timedelta
import datetime

# try:
quandl.ApiConfig.api_key = 'L4mLbs2qgHyMqQEYVHLW'
a = input('Stock ID: ')
b = quandl.get('HKEX/' + a , start_date= datetime.date.today() - datetime.timedelta(days = 10), end_date=date.today())
print(b)
# except:
#     print('Error')