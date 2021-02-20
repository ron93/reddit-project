import requests
from telegram import *
from  telegram.ext import CommandHandler, Updater, CallbackContext
import re
import yaml
import os
import csv

#bot = telegram.Bot(token='1641440572:AAE6XodFCsJSgSKLdJcnUZZyvXUKirHq10k')

#bot.send_photo(chat_id=390679456 ,photo=open('./../data/images/earthporn_picsljr6sy.jpg','rb'))
base_path = os.path.dirname(os.path.abspath(__file__))
config = yaml.load(open(os.path.join(base_path,'config.yaml')).read(),Loader=yaml.FullLoader)
token=config['general']['token']

bot = Bot(token)

def get_reddit():
    r = []
    with open("../../data/csv/earthporn_post.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            r.append(line)
        return r

def test(update:Update, context:CallbackContext):
    chat_id = update.effective_chat.id
    
    bot.send_photo(chat_id=chat_id, photo=open('../../data/piv.jpg', 'rb'))

def reddits(update:Update,context:CallbackContext):
    
    r = get_reddit()
    for i in r:
        bot.send_message(
            chat_id = update.effective_chat.id,
            text = i
         )

def main():
    
    updater = Updater(token=config['general']['token'], use_context = True)
    dispacher = updater.dispatcher
    start_value = CommandHandler('motion', test)
    red = CommandHandler('r', reddits)

    #dispacher.add_handler(CommandHandler('bop',bop))
    dispacher.add_handler(start_value)
    dispacher.add_handler(red)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    
    main()