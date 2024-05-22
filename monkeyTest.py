import telebot
from telebot import types
import webbrowser
import time

bot = telebot.TeleBot('7106621173:AAE7kIT1AQcDgRIHD94DyuKnPyYrQMCfznM')

user_data = {}

questions = [
    "What color do you prefer?",
    "Are you an introvert or extrovert?"
]

monkeyType = [
    {"name": "Such a cool monkey with a cool yellow Hawaiian shirt!", "color": "Yellow", "psychtype": "Extrovert"},
    {"name": "Such a sleepy monkey with a cute yellow blanket!", "color": "Yellow", "psychtype": "Introvert"},
    {"name": "Such a cool monkey with a nice pink dress!", "color": "Pink", "psychtype": "Extrovert"},
    {"name": "Such a sleepy monkey with a cool pink pajama!", "color": "Pink", "psychtype": "Introvert"}
]

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
        bot.send_message(message.chat.id, 'Let\'s start the test', parse_mode='html')
        user_data[message.chat.id] = {}
        send_question(message.chat.id, 0)
    elif message.text == 'Author':
        bot.send_message(message.chat.id, 'Welcome to my website!', parse_mode='html')
        time.sleep(1.0)
        webbrowser.open('https://google.com')
    elif message.text == 'Donation':
        webbrowser.open('https://savelife.in.ua/en')
    elif message.text == 'Leave review':
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

def send_question(chat_id, question_index):
    if question_index < len(questions):
        question = questions[question_index]
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        
        if question_index == 0:
            btn1 = types.KeyboardButton('Yellow')
            btn2 = types.KeyboardButton('Pink')
            markup.row(btn1, btn2)
        elif question_index == 1:
            btn1 = types.KeyboardButton('Introvert')
            btn2 = types.KeyboardButton('Extrovert')
            markup.row(btn1, btn2)
        
        bot.send_message(chat_id, question, reply_markup=markup)
        bot.register_next_step_handler_by_chat_id(chat_id, lambda msg: handle_answers(msg, question_index))
    else:
        send_result(chat_id)

def handle_answers(message, question_index):
    chat_id = message.chat.id
    if chat_id not in user_data:
        user_data[chat_id] = {}
    
    if question_index == 0:
        user_data[chat_id]['color'] = message.text
    elif question_index == 1:
        user_data[chat_id]['psychtype'] = message.text
    
    send_question(chat_id, question_index + 1)

def send_result(chat_id):
    user_answers = user_data.get(chat_id, {})
    color = user_answers.get('color')
    psychtype = user_answers.get('psychtype')

    result = next((monkey for monkey in monkeyType if monkey['color'] == color and monkey['psychtype'] == psychtype), None)
    
    if result:
        bot.send_message(chat_id, result['name'])
    else:
        bot.send_message(chat_id, 'Sorry, we could not find a match for your preferences.')

        # Show the main menu again after the test
    time.sleep(0.5)
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Start the test')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Author')
    btn3 = types.KeyboardButton('Donation')
    markup.row(btn2, btn3)
    btn4 = types.KeyboardButton('Leave review')
    markup.row(btn4)
    bot.send_message(chat_id, 'What would you like to do next?', reply_markup=markup)
    bot.register_next_step_handler_by_chat_id(chat_id, on_click)

@bot.message_handler(commands=['author'])
def author(message):
    bot.send_message(message.chat.id, 'Welcome to my website!', parse_mode='html')
    time.sleep(1.0)
    webbrowser.open(url='https://google.com')

@bot.message_handler(commands=['donation'])
def donation(message):
    bot.send_message(message.chat.id, 'Thank you for supporting Ukraine! 🇺🇦', parse_mode='html')
    time.sleep(1.0)
    webbrowser.open(url='https://savelife.in.ua/en/')

@bot.message_handler(commands=['review'])
def review(message):
    bot.send_message(message.chat.id, 'Please leave feedback 💭\nYour thoughts mean a lot to me!', parse_mode='html')
    time.sleep(3.0)
    webbrowser.open(url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')

bot.polling(none_stop=True)