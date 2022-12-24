from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint as rd


bot = Bot(token='5')
updater = Updater(token='5')
dispatcher = updater.dispatcher


A = 0
B = 1


def start(update, context):
    context.bot.send_message(update.effective_chat.id,"Привет, как у вас дела?")
    return A

def howareyou(update, context):
    text = update.message.text
    if 'хор' in text.lower():
     context.bot.send_message(update.effective_chat.id,"Я рад, что у тебя всё хорошо")
    else:
     context.bot.send_message(update.effective_chat.id,"Не грусти, всё будет отлично")
     context.bot.send_message(update.effective_chat.id,"Как погода?")
    return B
def weather(update, context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id,"И у меня такая же погода")
    return ConversationHandler.END


def func(update, context):
    text = update.message.text
    if 'прив' in text.lower():
     context.bot.send_message(update.effective_chat.id,"И тебе привет, мой дорогой друг!")
    else:
     context.bot.send_message(update.effective_chat.id,"Я тебя не понимаю ;(")

def cancel(update, context):
    context.bot.send_message(update.effective_chat.id,"Прощай")

start_handler = CommandHandler('start', start)
howareyou_handler = MessageHandler(Filters.text, howareyou)
weather_handler = MessageHandler(Filters.text, weather)
cancel_handler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(entry_points=[start_handler],
states={A: [howareyou_handler],
B: [weather_handler]
},
fallbacks=[cancel_handler]
)

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()