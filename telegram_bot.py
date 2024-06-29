import json

from telegram import *
# from telegram.ext import Updater
# from telegram.ext import CommandHandler
from telegram.ext import *
from tracker import get_prices
from requests import *
# from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



telegram_bot_token = "5592239864:AAHV73shOzgbPF4iPlEoqZKHB2c9aR9mniE"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


button1 = InlineKeyboardButton(text="👋 button1", callback_data="randomvalue_of10")
button2 = InlineKeyboardButton(text="💋 button2", callback_data="randomvalue_of100")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)
print(type(keyboard_inline))
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("👋 Hello!", "💋 Youtube")



def start(update,context):
    # buttons = [[KeyboardMarkup("/start")],[KeyboardMarkup("/price")],[KeyboardMarkup("/help")]]
    # # buttons = [KeyboardButton("/start"),KeyboardButton("/price"),KeyboardButton("/help")]
    # keyboard = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(buttons[0]).add(buttons[1]).add(buttons[2])

    # =[
    #     [
    #         KeyboardButton(text='button')
    #     ]
    reply_markup = ReplyKeyboardMarkup(keyboard=json.dumps(keyboard_inline), resize_keyboard=True)
    update.message.reply_text(reply_markup = json.dumps(reply_markup), text = 'start')
    # , reply_markup = reply_markup
    # text = 'start'



    # context.bot.send_message(chat_id=update.effective_chat.id,text="Hello ! Welcome to crypto king bot..",reply_markup=keyboard1)
    # update.message.reply_text("""
    # Hello ! Welcome to crypto king bot ...\n\nUse /help for more info.
    # """)


def help(update, context):
    update.message.reply_text("""
    Available comands are :\n
    /start -> Welcome message.
    /price -> For Cyptocurency price alert.
    /help -> For user help.
    """)


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text("Use /help for more info.")#update.message.text


def price(update, context):
    print('context:', context)
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        change_day = crypto_data[i]["change_day"]
        change_hour = crypto_data[i]["change_hour"]
        message += f"Coin: {coin}\nPrice: ${price:,.2f}\nHour Change: {change_hour:.3f}%\nDay Change: {change_day:.3f}%\n\n"

    context.bot.send_message(chat_id=chat_id, text=message)


# a="^/(?!start$)[a-z0-9]+$"
# def message():
#     return "Sorry this command is not available"
# # options = 'start'

dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler("start", start)],states={'price':[(CommandHandler("price", price))]},fallbacks=[(CommandHandler("help", help))]))
dispatcher.add_handler(CommandHandler("price", price))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.start_polling()

# dispatcher.add_handler(CommandHandler("help", help))
# updater.start_polling()

# dispatcher.add_handler(CommandHandler(a, message))
# updater.start_polling()
# while True:
#     cmd=""
#     if(cmd="start"):
#         dispatcher.add_handler(CommandHandler("start", start))
#         updater.start_polling()
#     else:
#