from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint as rd

#token = '5695592994:AAHMT7oC6SSPq8glVCILaZwxaXGo5xufQHA'
bot = Bot(token='5695592994:AAHMT7oC6SSPq8glVCILaZwxaXGo5xufQHA')
updater = Updater(token='5695592994:AAHMT7oC6SSPq8glVCILaZwxaXGo5xufQHA')
dispatcher = updater.dispatcher



def start(update, context):
    context.bot.send_message(update.effective_chat.id,"Hello")


def rand(update, context):
    context.bot.send_message(update.effective_chat.id,f'{rd(1,100)}')

#def func(update, context):
    #text= update.message.text
    #if 'прив' in text.lower():
        #context.bot.send_message(update.effective_chat.id,"И тебе привет")
    #else:
        #context.bot.send_message(update.effective_chat.id,"Я тебя не понимаю")

def find(update, context):
    text= update.message.text
    find_txt = "абв"
    lst = [i for i in text.split() if find_txt not in i]
    context.bot.send_message (update.effective_chat.id,f'Результат: {" ".join(lst)}')
          

start_handler = CommandHandler('start', start)
random_handler = CommandHandler ('random', rand)
#message_handler= MessageHandler (Filters.text, func)
find_handler = MessageHandler (Filters.text, find)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(random_handler)
#dispatcher.add_handler(message_handler)
dispatcher.add_handler(find_handler)


updater.start_polling()
updater.idle()