import datetime
from datetime import date,time,timedelta
import csv
import random
import webbrowser
data = {}
sport = ['football','basketball']
food = ['tea','burger','fries']
typ = []
ran = []
with open("bigdata.csv") as q:
    dataing = csv.DictReader(q, delimiter=',')
    for row in dataing:
        # ran.append(row['data'])
        ran.append(row['tag'])
    r = random.choice(ran)
    while r == 'unknown':
        r = random.choice(ran)
    print('Try searching for ' + random.choice(ran))
a = input('How do you feel ? ')


if a in sport:
    typ.append('sport')
elif a in food:
    typ.append('food')
else:
    typ.append('unknown')


with open('bigdata.csv','a+') as e:
    write = csv.writer(e, delimiter=',')
    write.writerow([a,datetime.datetime.now().time(),typ[0]])
    typ = []

webbrowser.open('www.google.com/#q=' + str(a))