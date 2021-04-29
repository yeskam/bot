from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton, ReplyKeyboardMarkup

inline_key = InlineKeyboardMarkup()

btn = InlineKeyboardButton('Да',callback_data='yes')
btn1 = InlineKeyboardButton('Нет',callback_data='no')

inline_key.add(btn,btn1)