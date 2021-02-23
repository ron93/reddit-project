import requests
from telegram import *
from  telegram.ext import CommandHandler, Updater, CallbackContext
import re
import yaml
import os
import csv
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

base_path = os.path.dirname(os.path.abspath(__file__))
config = yaml.load(open(os.path.join(base_path,'config.yaml')).read(),Loader=yaml.FullLoader)
token=config['general']['token']

bot = Bot(token)

def get_reddit():
    r = []
    with open("../../data/csv/earthporn_post.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for line in reader:
            r.append(line)
        return r

def test(update:Update, context:CallbackContext):
    chat_id = update.effective_chat.id
    
    bot.send_photo(chat_id=chat_id, photo=open('../../data/piv.jpg', 'rb'))

def reddits(update:Update,context:CallbackContext):
    sub = context.args
    r = get_reddit()
    for i in r:
        bot.send_message(
            chat_id = update.effective_chat.id,
            text = sub
         )

def get_sub(update:Update,context:CallbackContext):
    sub = context.args
    bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'getting reddits from { sub }'
         )
    return sub
    
def start_handler(update:Update, context:CallbackContext):
    logger.info("User {} started bot")
    update.message.reply_text("Hello from reddit bot!\nPress /r 'sub' to get sub reddits")


def main():
    
    updater = Updater(token=config['general']['token'], use_context = True)
    dispacher = updater.dispatcher
    start_value = CommandHandler('start', start_handler)
    #red = CommandHandler('r', reddits, pass_args=True )
    sub = CommandHandler('r', get_sub, pass_args=True )

    #dispacher.add_handler(CommandHandler('bop',bop))
    dispacher.add_handler(start_value)
    dispacher.add_handler(sub)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    
    main()