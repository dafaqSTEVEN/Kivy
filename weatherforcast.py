import xml.etree.ElementTree as ET
from urllib.request import urlopen
from bs4 import BeautifulSoup,CData
from lxml import etree
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
fp = open('logz.txt','w+')
response = urlopen('https://rss.weather.gov.hk/rss/CurrentWeather.xml')
html = response.read()
# soup =BeautifulSoup(html,'xml')
# description_tags = soup.find_all('CDATA')
# for tag in description_tags:
#     print(tag.string)
#     fp.write(str(tag.string) + '\n---------------------------------------------\n')



# print(str(soup.text))

soup = BeautifulSoup(html,'lxml')
fp.write(str(soup.text))
fp.close()

i = False
with open('logz.txt','r+') as var:
    for line in var:
        line = line.replace('  ','')
        line = line.replace('\n', '')
        line = line.replace('\r', '')
        line = line.replace('\r\n', '')
        line = line.replace('  ', '')
        line = line.replace('\t', '')
        line = line.replace('\0', '')

        if 'updated' in line:
            print(line)
        if 'Air temperature' in line:
            print(line)
        if 'Humidity' in line:
            print(line)
        if 'The air' in line:
            i = True
        if ']]>' in line:
            pass
        elif i == True and line != '':
            print(str(line)+'\n-------------------')

