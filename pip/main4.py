from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint as rd



bot = Bot(token='5695592994:AAHMT7oC6SSPq8glVCILaZwxaXGo5xufQHA')
updater = Updater(token='5695592994:AAHMT7oC6SSPq8glVCILaZwxaXGo5xufQHA')
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id,"Р—РґСЂР°РІСЃС‚РІСѓР№С‚Рµ!\nРЎРґРµР»Р°Р№С‚Рµ Р’Р°С€Сѓ СЃС‚Р°РІРєСѓ")
    

def bet(update, context):
    deposit = int(update.message.text)
    screen = generate_combos()
    win_money = deposit * count_token(screen)
    context.bot.send_message(update.effective_chat.id, game_board(screen))
    context.bot.send_message(update.effective_chat.id, win_money)

def generate_combos():
    screen = ''
    for i in range(12):
        screen += win_symbol[rd(0, len(win_symbol)-1)]
    return screen

tokens = {'рџЌЋ' : 1.1, 'рџЄІ' : 1.8, 'рџЌ†' : 2, 'рџЌ‹' : 3}

win_symbol = 'рџЌЋ'*5 + 'рџЄІ'*4 + 'рџЌ†'*2 + 'рџЌ‹' 



def check_win(token, value, screen):
    win_counter = 0
    for i in range(3):
        if screen[0+i*4] == screen[4*i+1] == screen[4*i+2] == screen[4*i+3] == token:
            win_counter += 1.5
    for i in range(4):
        if screen[i] == screen[i+4] == screen[i+8] == token:
            win_counter += 1
    return win_counter * value

def game_board(screen):
    
    string = '|'.join(screen[:4]) + '\n' + '|'.join(screen[4:8]) + '\n' + '|'.join(screen[8:])
    return string

def count_token(screen):
    sum_combo = 0
    
    for token, value in tokens.items():
        sum_combo += check_win(token, value, screen)
    return sum_combo


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id,"РџСЂРѕС‰Р°Р№")

start_handler = CommandHandler('start', start)
bet_handler = MessageHandler(Filters.text, bet)
# howareyou_handler = MessageHandler(Filters.text, howareyou)
# weather_handler = MessageHandler(Filters.text, weather)
# cancel_handler = CommandHandler('cancel', cancel)
# conv_handler = ConversationHandler(entry_points=[start_handler],
                                    # states={A: [howareyou_handler],
                                    # B: [weather_handler]
                                    # },
                                    # fallbacks=[cancel_handler]
                                    # )

dispatcher.add_handler(start_handler)
dispatcher.add_handler(bet_handler)

updater.start_polling()
updater.idle()