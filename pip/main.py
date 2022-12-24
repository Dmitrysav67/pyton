from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint as rd

#token = '569'
bot = Bot(token='56')
updater = Updater(token='56')
dispatcher = updater.dispatcher



def start(update, context):
    context.bot.send_message(update.effective_chat.id,"Hello")


def rand(update, context):
    context.bot.send_message(update.effective_chat.id,f'{rd(1,100)}')

def func(update, context):
    text= update.message.text
    if 'прив' in text.lower():
        context.bot.send_message(update.effective_chat.id,"И тебе привет")
    else:
        context.bot.send_message(update.effective_chat.id,"Я тебя не понимаю")

start_handler = CommandHandler('start', start)
random_handler = CommandHandler ('random', rand)
message_handler= MessageHandler (Filters.text, func)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(random_handler)
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()