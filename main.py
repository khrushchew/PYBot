# My import for a message
from welcome_message import a

# Import for a telebot
import telebot
import webbrowser

# More and more import
from random import choice

bot = telebot.TeleBot('6691756516:AAHN4XIDmeIJ_Qk1dkDIYe97ce8hqE4MgGQ')


@bot.message_handler(commands=['website'])
def site(message):
    webbrowser.open("https://www.kinopoisk.ru")


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'''Hi, {message.from_user.first_name}! {choice(a)}''')


@bot.message_handler(commands=['help'])
def main(message):
    with open('Help.txt', 'r', encoding='Utf-8') as help_file:
        bot.send_message(message.chat.id, help_file.read())


@bot.message_handler(content_types=['photo', 'video', 'audio', 'text'])
def error(message):
    bot.reply_to(message, "Error... Unknown command!")


bot.infinity_polling()
