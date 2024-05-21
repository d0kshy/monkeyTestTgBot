import telebot
from telebot import types
import webbrowser
import time

bot = telebot.TeleBot('7106621173:AAE7kIT1AQcDgRIHD94DyuKnPyYrQMCfznM')

user_data = {}

questions = [
    "What color do you prefer? (Yellow/Pink)",
    "Are you introvert or extrovert? (Introvert/Extrovert)"
]

monkeyType = [
    {"name": "YellowParty", "color": "Yellow", "psychtype": "Extrovert"},
    {"name": "YellowSleep", "color": "Yellow", "psychtype": "Introvert"},
    {"name": "PinkParty", "color": "Pink", "psychtype": "Extrovert"},
    {"name": "PinkSleep", "color": "Pink", "psychtype": "Introvert"}
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
        bot.send_message(message.chat.id, 'Let\'s start the test:', parse_mode='html')
        user_data[message.chat.id] = {'question_index': 0}
        bot.send_message(message.chat.id, questions[0])
        bot.register_next_step_handler(message, handle_answers)
    elif message.text == 'Author':
        bot.send_message(message.chat.id, 'Welcome to my website!', parse_mode='html')
        time.sleep(1.0)
        webbrowser.open('https://google.com')
    elif message.text == 'Donation':
        webbrowser.open('https://savelife.in.ua/en')
    elif message.text == 'Leave review':
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

@bot.message_handler(func=lambda message: message.chat.id in user_data)
def handle_answers(message):
    chat_id = message.chat.id
    answer = message.text.strip().lower()
    
    question_index = user_data[chat_id]['question_index']
    
    if question_index == 0:
        if answer == "yellow" or answer == "pink":
            user_data[chat_id]['color'] = answer.capitalize()
        else:
            bot.send_message(chat_id, "Please choose a valid color: Yellow or Pink")
            bot.register_next_step_handler(message, handle_answers)
            return
    elif question_index == 1:
        if answer == "introvert" or answer == "extrovert":
            user_data[chat_id]['psychtype'] = answer.capitalize()
        else:
            bot.send_message(chat_id, "Please choose a valid type: Introvert or Extrovert")
            bot.register_next_step_handler(message, handle_answers)
            return
    
    question_index += 1
    if question_index < len(questions):
        user_data[chat_id]['question_index'] = question_index
        bot.send_message(chat_id, questions[question_index])
        bot.register_next_step_handler(message, handle_answers)
    else:
        selected_monkeyType = select_monkeyType(user_data[chat_id])
        bot.send_message(chat_id, f"Here is your result: {selected_monkeyType['name']}")
        user_data.pop(chat_id)

def select_monkeyType(user_data):
    for monkey in monkeyType:
        if (user_data['color'] == monkey['color'] and 
            user_data['psychtype'] == monkey['psychtype']):
            return monkey
    return {"name": "There is no your type of monkey."}

@bot.message_handler(commands=['author'])
def author(message):
    bot.send_message(message.chat.id, 'Welcome to my website!', parse_mode='html')
    time.sleep(1.0)
    webbrowser.open('https://google.com')

@bot.message_handler(commands=['donation'])
def donation(message):
    bot.send_message(message.chat.id, 'Thank you for supporting Ukraine! 🇺🇦', parse_mode='html')
    time.sleep(1.0)
    webbrowser.open('https://savelife.in.ua/en/')

@bot.message_handler(commands=['review'])
def review(message):
    bot.send_message(message.chat.id, 'Please leave feedback 💭\nYour thoughts mean a lot to me!', parse_mode='html')
    time.sleep(3.0)
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

bot.polling(none_stop=True)
