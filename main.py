#Бот для получения погоды made by zzsxd
import telebot
import requests
import json

bot = telebot.TeleBot('6736692677:AAFLu-4SrE-rvh2WgrCliGvoSWCP7QaaXCI')
API = 'f84ac7ee3309c7da133cba71e82865fe'

@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id, 'Привет! Где ты живешь?')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot.reply_to(message, f"Сейчас погода: {data['main']['temp']}")
    else:
        bot.reply_to(message, 'Неправильно указан город')


bot.polling(none_stop=True)