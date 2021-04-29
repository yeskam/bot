import telebot

from random import randint
from decouple import config
from keyboards.inline_keyboard import inline_key as in_key

bot = telebot.TeleBot(config('TOKEN'))

number = randint(1, 10)
attempts = 0

@bot.message_handler(commands=['start', ])
def welcome(message):
    bot.send_message(message.chat.id, 'Угадай число от 1 до 10,у тебя есть 5 попыток')


@bot.message_handler(content_types=['text'])
def start_text(message):
    chat_id = message.chat.id
    global number
    global attempts
    if int(message.text) != number:
        attempts += 1
        if int(message.text) - 1 == number or int(message.text) + 1 == number:
            bot.send_message(chat_id, 'Близко')
        else:
            bot.send_message(chat_id, 'холодно')
            bot.send_message(chat_id, f'ты промахнулся {attempts} раз')
        if attempts == 5:
            bot.send_message(chat_id, 'Ты проиграл,хочешь еще поиграть?', reply_markup=in_key)
            attempts = 0
    elif int(message.text) == number:
        bot.send_message(chat_id, 'Ты угадал,хочешь еще поиграть?', reply_markup=in_key)
        attempts = 0


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    chat_id = call.message.chat.id
    if call.data == 'yes':
        global number
        number = randint(1, 10)
        msg = bot.send_message(chat_id, 'Eще раз,угадай число от 1 до 10,у тебя есть 5 попыток!')
        bot.register_next_step_handler(msg, start_text)

    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Окей')


bot.polling(none_stop=True)