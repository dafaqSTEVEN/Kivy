import logging
from telegram.ext import Updater, MessageHandler, CommandHandler, RegexHandler, CallbackQueryHandler,ConversationHandler,Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup
import os
import xml.etree.ElementTree as ET
from datetime import date,timedelta
import pandas as pd
import datetime
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup,CData
from lxml import etree
import quandl
import os
import json

import csv
dir_path = os.path.dirname(os.path.realpath(__file__))

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
    # x = ''.join(soup.text.split())
    fp.write(soup.text)
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

def location(bot,update):
    location_keyboard = [[KeyboardButton(text="send_location",  request_location=True)]]
    update.message.reply_text('Tell me your location',reply_markup = ReplyKeyboardMarkup(location_keyboard,one_time_keyboard=True))

def send_location(bot,update):
    update.message.reply_text(str(update.message.location.latitude) +'\n'+str(update.message.location.longitude))

def main():
    updater = Updater("886726378:AAGzZp3SJ5tk1jd1lc5ggIkVsNKmibd5OjU")
    assist = updater.dispatcher
    assist.add_handler(CommandHandler('start',start,pass_args = True))
    assist.add_handler(RegexHandler('.*status.*',status))
    assist.add_handler(RegexHandler('.*weather.*',weather))
    assist.add_handler(RegexHandler('.*location.*',location))
    assist.add_handler(MessageHandler(Filters.location,send_location))
    assist.add_handler(ConversationHandler(entry_points = [RegexHandler('.*stock.*',id)],states = {ID:[RegexHandler('.*.*',id)],DATE:[RegexHandler('.*.*',day)],STOCK_CHECK:[RegexHandler('.*.*',stock)]},fallbacks = [CommandHandler('cancel',CANCEL)]))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

