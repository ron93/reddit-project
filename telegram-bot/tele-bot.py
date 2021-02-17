import requests
from telegram import *
from  telegram.ext import CommandHandler, Updater, CallbackContext
import re
import yaml
import os

#bot = telegram.Bot(token='1641440572:AAE6XodFCsJSgSKLdJcnUZZyvXUKirHq10k')

#bot.send_photo(chat_id=390679456 ,photo=open('./../data/images/earthporn_picsljr6sy.jpg','rb'))
base_path = os.path.dirname(os.path.abspath(__file__))
config = yaml.load(open(os.path.join(base_path,'config.yaml')).read(),Loader=yaml.FullLoader)
token=config['general']['token']

bot = Bot(token)



def test(update:Update, context:CallbackContext):
    chat_id = update.effective_chat.id

    bot.send_photo(chat_id=chat_id, photo=open('../data/piv.jpg', 'rb'))


def main():
    
    updater = Updater(token=config['general']['token'], use_context = True)
    dispacher = updater.dispatcher
    start_value = CommandHandler('motion', test)
    #dispacher.add_handler(CommandHandler('bop',bop))
    dispacher.add_handler(start_value)
 
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    
    main()