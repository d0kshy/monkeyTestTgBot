import telebot
from telebot import types
import webbrowser
import time

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    time.sleep(0.5)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Start the test', callback_data='delete')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Author', url='https://google.com')
    btn3 = types.InlineKeyboardButton('Donation', url='https://savelife.in.ua/')
    markup.row(btn2, btn3)
    btn4 = types.InlineKeyboardButton('Leave review', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Hi there, {message.from_user.first_name}! Choose the option:', reply_markup=markup)

@bot.message_handler(commands=['author'])
def donation(message):
    bot.send_message(message.chat.id, 'Welcome to my website!', parse_mode='html')
    time.sleep(1.0)
    webbrowser.open(url='https://google.com')

@bot.message_handler(commands=['donation'])
def donation(message):
    bot.send_message(message.chat.id, 'Thank you for supporting Ukraine! 🇺🇦', parse_mode='html')
    time.sleep(1.0)
    webbrowser.open(url='https://savelife.in.ua/')

@bot.message_handler(commands=['review'])
def donation(message):
    bot.send_message(message.chat.id, 'Please leave feedback 💭\nYour thoughts means a lot to me!', parse_mode='html')
    time.sleep(3.0)
    webbrowser.open(url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')

bot.polling(none_stop=True)