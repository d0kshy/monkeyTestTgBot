import telebot
from telebot import types
import webbrowser
import time

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    time.sleep(0.5)
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Start the test')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Author')
    btn3 = types.KeyboardButton('Donation')
    markup.row(btn2, btn3)
    btn4 = types.KeyboardButton('Leave review')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Hi there, {message.from_user.first_name}! Choose the option:', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Start the test':
        pass
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Author':
        webbrowser.open('https://google.com')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Donation':
        webbrowser.open('https://savelife.in.ua/')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Donation':
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        bot.register_next_step_handler(message, on_click)

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
