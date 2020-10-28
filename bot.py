# COMMON
import os
# 3RD PARTY
import telebot
# CUSTOM
from spider import search_spider

# TOKEN TO BE REPLACED WITH OS VARIABLE
TOKEN = os.environ.get('SRSB_TOKEN')

# BOT INSTANCE
bot = telebot.TeleBot(TOKEN)

latest_search = []

# DEFAULT COMMANDS HANDLER
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, 'Howdy, how are you doing?')

@bot.message_handler(commands=['latest'])
def last_query(message):
    bot.reply_to(message, str(latest_search))

# SEARCH QUERY HANDLER
@bot.message_handler(func=lambda m: True)
def search_series(message):
    global latest_search
    latest_search = search_spider(str(message.text))
    bot.reply_to(message, str(latest_search))

bot.polling()