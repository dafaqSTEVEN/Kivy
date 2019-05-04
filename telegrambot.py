import logging
from telegram.ext import Updater, MessageHandler, CommandHandler, RegexHandler, CallbackQueryHandler,ConversationHandler,Filters,InlineQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove,message,Message
from uuid import uuid4

from telegram import InlineQueryResultArticle, ParseMode,InputTextMessageContent
from telegram.utils.helpers import escape_markdown
import os
import xml.etree.ElementTree as ET
from datetime import date,timedelta
# import pandas as pd
import datetime
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup,CData
from lxml import etree
import quandl
import os
import json
from time import strftime
import feedparser
import csv,random
from random import randint
import pyshorteners
from pyshorteners import Shorteners

# API_USER = "uesaka"
# API_KEY = "R_3f898a33b09a4334897c1778cbc091be"
#
# b = bitly_api.Connection(API_USER, API_KEY)
dir_path = os.path.dirname(os.path.realpath(__file__))

starting_time = time.time()
ending_time = starting_time + 20
print('\rLoading data...')
exec(open(dir_path + '\\agency.py').read())
exec(open(dir_path + '\\fare_attributes.py').read())
exec(open(dir_path + '\\fare_rules.py').read())
exec(open(dir_path + '\\frequencies.py').read())
exec(open(dir_path + '\\route.py').read())
exec(open(dir_path + '\\stop.py').read())
exec(open(dir_path + '\\trips.py').read())
exec(open(dir_path + '\\stop_time.py').read())
print("Time usage : " + str(round(time.time() - starting_time, 3)) + ' seconds.\n')

trip_route_convertion = []

newsarray = []

NewsFeed = feedparser.parse("https://rthk.hk/rthk/news/rss/c_expressnews_clocal.xml")
def button(bot,update):
    query = update.callback_query
    for i in range(len(NewsFeed)):
        if query.data == ('news' + str(i)):
            bot.edit_message_text(chat_id = update.effective_message.chat_id,message_id = update.effective_message.message_id,text = str(NewsFeed.entries[i].title) + '\n---------------------\nLink : ' + str(NewsFeed.entries[i].link) +'\n---------------------\n' + str(NewsFeed.entries[i].summary) + '\n---------------------\nPublished on :' + str(NewsFeed.entries[i].published))

def news(bot,update):
    keyboard = [[]]
    global news,message_id
    update.message.reply_text('<Local News>')
    for i in range(len(NewsFeed)):
        newsarray.append('Title : ' + NewsFeed.entries[i].title)
        newsarray.append('Link : ' +NewsFeed.entries[i].link)
        newsarray.append('Published date : ' + NewsFeed.entries[i].published)
        newsarray.append('---------------------\nType : Local News')
        keyboard.append([InlineKeyboardButton('Detail: '+ str(NewsFeed.entries[i].title),callback_data= ('news'+str(i)))])
        bot.sendMessage(text = '\n'.join(newsarray),chat_id=update.message.chat_id,disable_web_page_preview = True ,reply_markup = InlineKeyboardMarkup(keyboard))
        keyboard = [[]]
        newsarray.clear()







print('Running ' + time.ctime(time.time()))

weathers = []
nominal_price = []
net_change = []
change = []
bid = []
ask = []
pex = []
high = []
low = []
previous = []
share_volume = []
turnover = []
lot_size = []


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='logging.txt',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# exec (open(dir_path + '\\stock.py').read())

def weather(bot,update):
    fp = open('logz.txt', 'w+')
    response = urlopen('https://rss.weather.gov.hk/rss/CurrentWeather.xml')
    html = response.read()

    soup = BeautifulSoup(html, 'lxml')
    x = soup.text.replace('\xa0','')
    fp.write(x)
    fp.close()

    i = False
    with open('logz.txt', 'r+') as var:
        for line in var:
            line = line.replace('  ', '')
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            line = line.replace('\r\n', '')
            line = line.replace('  ', '')
            line = line.replace('\t', '')
            line = line.replace('\0', '')

            if 'updated' in line:
                update.message.reply_text(line)
            if 'Air temperature' in line:
                update.message.reply_text(line)
            if 'Humidity' in line:
                update.message.reply_text(line)
            if 'UV Index' in line:
                update.message.reply_text(line)
            if 'UV radiation' in line:
                update.message.reply_text(line)
            if 'The air' in line:
                i = True
            if ']]>' in line:
                pass
            elif i == True and line != '':
                weathers.append(str(line + '\n'))
    update.message.reply_text(''.join(weathers))

ID , DATE ,STOCK_CHECK = range(3)

def id(bot,update,use_context = True):
    update.message.reply_text('Tell me the stock ID\nThe stock ID must be input as a 5-digit format(e.g 83079)\nType /cancel to exit')
    return DATE

def day(bot,update,use_context = True):
    global stock_id
    stock_id = update.message.text
    if stock_id == '/cancel':
        update.message.reply_text('Noted')
        return ConversationHandler.END
    update.message.reply_text('The stock ID you inputed is : '+stock_id)
    update.message.reply_text('Now tell me from how many days ago you want to know the info about.\ntype /cancel to exit')
    return STOCK_CHECK

stockkk = []

def stock(bot,update,use_context = True):
    global stock_date
    stock_date = update.message.text
    if stock_date == '/cancel':
        update.message.reply_text('Noted')
        return ConversationHandler.END
    update.message.reply_text('The starting date you enter is ' + str(datetime.date.today() - datetime.timedelta(days=int(stock_date))))
    quandl.ApiConfig.api_key = 'KVPSsy7GuZrgRNx9Gxhd'
    # with open('stock.csv', 'w+') as stocking:
        # try:
        #     df = pd.DataFrame(quandl.get('HKEX/' + stock_id, start_date=datetime.date.today() - datetime.timedelta(days=int(stock_date)),end_date=date.today()))
        #     stocking.write(df.to_csv(index =False))
    data = (quandl.get('HKEX/' + stock_id, start_date=datetime.date.today() - datetime.timedelta(days=int(stock_date)),end_date=date.today())).to_string()
    update.message.reply_text(data.replace('\n','\n--------------------------------------------------------------\n'))
        # except:
        #     update.message.reply_text('Something went wrong\nPleease try again.')
        #     return ConversationHandler.END
    # with open('stock.csv') as stocking:
    #     stock_data = csv.DictReader(stocking, delimiter=',')
    #     for row in stock_data:
    #         nominal_price.append(row['Nominal Price'])
    #         net_change.append(row['Net Change'])
    #         change.append(row['Change (%)'])
    #         bid.append(row['Bid'])
    #         ask.append(row['Ask'])
    #         pex.append(row['P/E(x)'])
    #         high.append(row['High'])
    #         low.append(row['Low'])
    #         previous.append(row['Previous Close'])
    #         share_volume.append(row['Share Volume (000)'])
    #         turnover.append(row['Turnover (000)'])
    #         lot_size.append(row['Lot Size'])
    #
    # update.message.reply_text('|Nominial Price|Net Change|Change(%)|Bid|Ask|P/E(x)|High|Low|Previous Close|Share Volume(000)|Turnover(000)|Lot Size|\n')



    return ConversationHandler.END

def CANCEL(bot,update,use_context = True):
    update.message.reply_text('Noted.')
    return ConversationHandler.END

def start(bot,update,args):
    update.message.reply_text('Thank you for using Assist.\nType /help for more info')


def status(bot,update):
    update.message.reply_text('Normal')



BUS,ASK_FOR,WHICH = range(3)

def bus_ask(bot,update,use_context = True):
    update.message.reply_text('Please tell me the route name : ')
    return ASK_FOR

temp = []
time_dict = {}
time_list = []
trip_1 = []
b = 0
single = True

def ask_for(bot,update,use_context =True):
    global temp
    a = update.message.text
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
        update.message.reply_text('No such route')

    update.message.reply_text('Search Result:')

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
        update.message.reply_text('Route ID : ' + str(e[0]) + '\nAgency ID : ' + str(e[1]) + '\nRoute name : ' + str(
            e[2]) + '\nRoute Full name : ' + str(e[3]) + '\nRoute type : ' + str(zz1) + '\nRoute URL : ' + str(
            e[5]) )
    if len(temp) > 1:
        update.message.reply_text('Select from result\nE.g. 1 (for the first result)')
        single = False
    return WHICH


def which(bot,update,use_context = True):
    global time_list
    global time_dict
    global single
    global b
    global trip_1
    if single != False:
        b = int(update.message.text)
    for key in trip.keys():
        if b == 0:
            if temp[b][0] in trip[key]:
                trip_route_convertion.append(key)
        elif temp[b - 1][0] in trip[key]:
            trip_route_convertion.append(key)
    list_time_id = []
    for i in range(len(trip_route_convertion)):
        list_time_id.append(trip_route_convertion[i].split('-')[3])
    print(list_time_id)
    print(trip_route_convertion)

    update.message.reply_text('The time now is: ' + strftime('%H%M'))
    for i in range(len(list_time_id)):
        t1 = timedelta(hours=int(strftime('%H')), minutes=int(strftime('%M')))
        t2 = timedelta(hours=int(list_time_id[i][0] + list_time_id[i][1]),
                       minutes=int(list_time_id[i][2] + list_time_id[i][3]))
        t3 = t2 - t1
        print(t3,t2,t1)
        if t3 > datetime.timedelta(minutes=0):
            time_list.append(t3)
        else:
            pass
        time_dict[str(t2)] = str(t3)
    t4 = min(time_list)
    print(t4)
    print(time_dict)
    for key in time_dict.keys():
        if str(t4) in time_dict[key]:
            update.message.reply_text('The next bus will arrive at : ' + key)
            break
        break

    for i in range(len(trip_route_convertion)):
        global trip_1
        for key in stop_time:
            if trip_route_convertion[i] == stop_time[key][0]:
                if [stop_time[key][3], stop_time[key][4]] not in trip_1:
                    trip_1.append([stop_time[key][3], stop_time[key][4]])
    # for i in range(len(trip_1)):
    #     update.message.reply_text('>The stop Name is ' + str(stop[trip_1[i][0]][1]) + ' (Stop ID:' + str(
    #         trip_1[i][0]) + ')' + '\n>' + 'The Stop Sequence is ' + str(trip_1[i][1] + '\n'))
    location_keyboard = [[KeyboardButton(text="send_location",  request_location=True)]]
    update.message.reply_text('Tell me your location to find the nearest stop.\nBe reminded that you have to allow Telegram or Telegram X to access your location in setting',reply_markup = ReplyKeyboardMarkup(location_keyboard,one_time_keyboard=True))
    return ConversationHandler.END

list_stop_location = {}

cal_lon = []
cal_lat = []
cal_dict = {}
def send_location(bot,update):
    global trip_1
    global cal_dict
    global cal_lat
    global cal_lon
    print(trip_1)
    long = update.message.location.longitude
    lat = update.message.location.latitude
    for i in range(len(trip_1)):
        for key in stop:
            print(stop[key])
            if trip_1[i][0] == stop[key][0]:
                list_stop_location[stop[key][0]] = [stop[key][2],stop[key][3]]
    print(list_stop_location)
    for key in list_stop_location:
        cal_lat.append(abs(float(list_stop_location[key][0]) - float(lat)))
        cal_lon.append(abs(float(list_stop_location[key][1]) - float(long)))
        cal_dict[key] = [abs(float(list_stop_location[key][0]) - float(lat)),abs(float(list_stop_location[key][1]) - float(long))]
    print(cal_lat)
    print(cal_lon)
    result_lat = min(cal_lat)
    result_long = min(cal_lon)
    print(result_lat)
    print(result_long)
    print(cal_dict)
    for key in (cal_dict):
        if result_lat == cal_dict[key][0]:
            update.message.reply_text('Nearest stop by Latitude is: ' + str(stop[key][1]))
        if result_long == cal_dict[key][1]:
            update.message.reply_text('Nearest stop by Longtitude is: '+  str(stop[key][1]))
    update.message.reply_text('Complete',reply_markup = ReplyKeyboardRemove(remove_keyboard = True))

ran = []
search_tag = False
search_subtag = False
type_list = ''
type_sub_list = ''
ran_answer = None
def gg(bot,update,user_data):
    global search
    search = update.message.text.partition(' ')[2].lower()
    with open("tag.csv") as q:
        table = csv.DictReader(q, delimiter=',')
        for row in table:
            global ran, type_list, type_sub_list
            if search == row['subtag']:
                type_list = row['tag']
                type_sub_list = row['subtag']
            if search == row['tag']:
                type_list = row['tag']
            if search == row['content']:
                type_list = row['tag']
                type_sub_list = row['subtag']
                ran.append(row['tag'])
                ran.append(row['subtag'])
        ran.append(search)
        print(ran)
    with open('tag.csv', 'a+',newline='') as g:
        data = csv.DictReader(g, delimiter=',')
        write = csv.writer(g, delimiter=',')
        global search_tag
        for row in data:
            if search != row['content']:
                pass
            else:
                search_tag = True
        if search_tag == False:
            write.writerow([search, datetime.datetime.now().time(), type_list, type_sub_list])
    update.message.reply_text('Try searching for ' + str(random.choice(ran)))
    longurl = 'https://www.google.com/#q=' + str(search)
    s = pyshorteners.Shortener(Shorteners.TINYURL)
    shorturl = s.short(longurl)
    update.message.reply_text('Search Result for ' + search.upper() + '\n' + str(shorturl))
    ran.clear()


def inline(bot,update,use_context = True):
    query = update.inline_query.query
    global ran, search, ran_answer
    ran.clear()
    with open("tag.csv") as q:
        table = csv.DictReader(q, delimiter=',')
        for row in table:
            global type_list, type_sub_list
            if ran_answer == row['subtag']:
                type_list = row['tag']
                type_sub_list = row['subtag']
            if ran_answer == row['tag']:
                type_list = row['tag']
            if ran_answer == row['content']:
                type_list = row['tag']
                type_sub_list = row['subtag']
                ran.append(row['tag'])
                ran.append(row['subtag'])
        ran.append(ran_answer)
        print(ran)
    with open('tag.csv', 'a+') as g:
        data = csv.DictReader(g, delimiter=',')
        write = csv.writer(g, delimiter=',')
        global search_tag
        for row in data:
            if ran_answer != row['content']:
                pass
            else:
                search_tag = True
        if search_tag == False:
            write.writerow([search, datetime.datetime.now().time(), type_list, type_sub_list])
            try :
                ran_answer = str(random.choice(ran))
                if ran_answer == '':
                    ran.remove(ran_answer)
            except ran_answer != '':
                pass
    print(ran_answer)
    update.message.reply_text('Try searching for ' + ran_answer)
    results = [
        InlineQueryResultArticle(
            id=query.id,
            title='Try searching for ' + str(random.choice(ran)),
            input_message_content=InputTextMessageContent(
                query.upper()))]
    print(results)
    update.inline_query.answer(results)
    ran.clear()


def thank(bot,update):
    update.message.reply_text("You're welcome.")

def main():
    updater = Updater("886726378:AAF9gwzWZzr0pfw-Wh5_bnnQHUybcOI6Z6g")
    assist = updater.dispatcher
    assist.add_handler(RegexHandler('.*news.*',news))
    assist.add_handler(CommandHandler('start',start,pass_args = True))
    assist.add_handler(RegexHandler('.*status.*',status))
    assist.add_handler(RegexHandler('.*weather.*',weather))
    assist.add_handler(MessageHandler(Filters.location,send_location))
    assist.add_handler(RegexHandler('.*thank.*',thank))
    assist.add_handler(CommandHandler('gg', gg,pass_user_data=True))
    assist.add_handler(InlineQueryHandler(inline,pass_user_data=True))
    assist.add_handler(ConversationHandler(entry_points =[RegexHandler('.*bus.*',bus_ask)],states ={BUS:[RegexHandler('.*.*',bus_ask)],ASK_FOR:[RegexHandler('.*.*',ask_for)],WHICH:[RegexHandler('.*.*',which)]},fallbacks=[CommandHandler('cancel',CANCEL)]))
    assist.add_handler(ConversationHandler(entry_points = [RegexHandler('.*stock.*',id)],states = {ID:[RegexHandler('.*.*',id)],DATE:[RegexHandler('.*.*',day)],STOCK_CHECK:[RegexHandler('.*.*',stock)]},fallbacks = [CommandHandler('cancel',CANCEL)]))
    assist.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

