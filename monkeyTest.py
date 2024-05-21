import telebot
from telebot import types
import webbrowser
import time

bot = telebot.TeleBot('TOKEN')

user_data = {}

questions = [
    "What color do you prefer?",
    "Are you introvert or exravert?"
]

monkeyType = [
    {"name": "YellowParty", "color": "Yellow", "psychtype": "Extravert"},
    {"name": "YellowSleep", "color": "Yellow", "psychtype": "Introvert"},
    {"name": "PinkParty", "color": "Pink", "psychtype": "Extravert"},
    {"name": "PinkParty", "color": "Pink", "psychtype": "Introvert"}
]

@bot.message_handler(commands=['start'])
def start(message):
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
        que1(message)
    elif message.text == 'Author':
        bot.send_message(message.chat.id, 'Welcome to my website!', parse_mode='html')
        time.sleep(1.0)
        webbrowser.open('https://google.com')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Donation':
        webbrowser.open('https://savelife.in.ua/en')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Leave review':
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        bot.register_next_step_handler(message, on_click)

def que1(message):
    markup = types.InlineKeyboardMarkup()
    btn2 = types.InlineKeyboardButton('Pink', callback_data='color_pink')
    btn3 = types.InlineKeyboardButton('Yellow', callback_data='color_yellow')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, f'What color would you prefer?', reply_markup=markup)


@bot.message_handler(commands=['author'])
def donation(message):
    bot.send_message(message.chat.id, 'Welcome to my website!', parse_mode='html')
    time.sleep(1.0)
    webbrowser.open(url='https://google.com')

@bot.message_handler(commands=['donation'])
def donation(message):
    bot.send_message(message.chat.id, 'Thank you for supporting Ukraine! 🇺🇦', parse_mode='html')
    time.sleep(1.0)
    webbrowser.open(url='https://savelife.in.ua/en/')

@bot.message_handler(commands=['review'])
def donation(message):
    bot.send_message(message.chat.id, 'Please leave feedback 💭\nYour thoughts means a lot to me!', parse_mode='html')
    time.sleep(3.0)
    webbrowser.open(url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')

bot.polling(none_stop=True)