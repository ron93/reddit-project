import requests
from telegram import *
from  telegram.ext import *
import re
import yaml
import os

#bot = telegram.Bot(token='1641440572:AAE6XodFCsJSgSKLdJcnUZZyvXUKirHq10k')

#bot.send_photo(chat_id=390679456 ,photo=open('./../data/images/earthporn_picsljr6sy.jpg','rb'))
base_path = os.path.dirname(os.path.abspath(__file__))
config = yaml.load(open(os.path.join(base_path,'config.yaml')).read(),Loader=yaml.FullLoader)
token=config['general']['token']
bot = Bot(token)

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def test(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id = update.effective_chat.id,
        text = "test sucessful!!",
    )

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