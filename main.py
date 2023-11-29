# My import for a message
from welcome_message import a

# Import for a telebot
import telebot
import webbrowser
from telebot import types

# More and more import
from random import choice

bot = telebot.TeleBot('6691756516:AAHN4XIDmeIJ_Qk1dkDIYe97ce8hqE4MgGQ')


@bot.message_handler(commands=['website'])
def site(message):
    webbrowser.open("https://www.kinopoisk.ru")


# def on_click(message):
#     if message.text == 'start':
#         bot.send_message(message.chat.id, choice(a))


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    button_for_start = types.KeyboardButton('/start')
    markup.add(button_for_start)
    bot.send_message(message.chat.id, choice(a), reply_markup=markup)
    # bot.register_next_step_handler(message, on_click)


@bot.message_handler(commands=['help'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    button_for_start = types.KeyboardButton('help')
    markup.add(button_for_start)
    with open('Help.txt', 'r', encoding='Utf-8') as help_file:
        bot.send_message(message.chat.id, help_file.read())


@bot.message_handler(content_types=['photo', 'video', 'audio', 'text'])
def error(message):
    bot.reply_to(message, "Ошибка... Неизвестная команда!")


bot.infinity_polling()
