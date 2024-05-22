import telebot
from telebot import types
import webbrowser
import time

bot = telebot.TeleBot('TOKEN')

user_data = {}

questions = [
    "What color do you prefer?",
    "Are you introvert or extrovert?"
]

monkeyType = [
    {"name": "Such a cool monkey with a cool yellow hawaiian shirt!", "color": "Yellow", "psychtype": "Extravert"},
    {"name": "Such a sleepy monkey with a cute yellow blanket!", "color": "Yellow", "psychtype": "Introvert"},
    {"name": "Such a cool monkey with a nice pink dress!", "color": "Pink", "psychtype": "Extravert"},
    {"name": "Such a sleepy monkey with a cool pink pijama!", "color": "Pink", "psychtype": "Introvert"}
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
        bot.register_next_step_handler(message, handle_answers)
        send_question(message.chat.id, 0)
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

def send_question(chat_id, question_index):
    question = questions[question_index]
    
    bot.send_message(chat_id, question)
    user_data[chat_id]['question_index'] = question_index


@bot.message_handler(func=lambda message: message.chat.id in user_data)
def handle_answers(message):
    chat_id = message.chat.id
    answer = message.text.lower()
    question_index = user_data[chat_id].get('question_index', 0)

    if question_index == 0:
        user_data[chat_id]['color'] = answer
    elif question_index == 1:
        user_data[chat_id]['psychtype'] = answer

    question_index += 1
    if question_index < len(questions):
        send_question(chat_id, question_index)
    else:
        selected_monkey = select_monkey(user_data[chat_id])
        bot.send_message(chat_id, f"Here is your result: {selected_monkey['name']}", reply_markup=types.ReplyKeyboardRemove())
        user_data.pop(chat_id)   


def select_monkey(user_data):
    for monkey in monkeyType:
        if (user_data['color'] == monkey['color'] and 
            user_data['psychType'] == monkey['psychType']):
            return monkey
    return {"name": "No monkey type found"}
 

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
