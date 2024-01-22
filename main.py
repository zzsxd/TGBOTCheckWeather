#############################################
#                created                    #
#                  by                       #
#                 zzsxd                     #
#       TelegramBotCheckTheWeather          #
#############################################
import telebot
import requests
import json
from telebot import types

bot = telebot.TeleBot('bot_api')
API = 'openweathermap_api'

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет👋\nЯ WeatherBot🌤 - могу дать информацию о погоде в любом городе!\nВведите /creators - чтобы узнать информацию о создателе бота.')
    bot.send_message(message.chat.id, 'Введите свой город, чтобы начать!')

@bot.message_handler(commands=['creators'])
def creators(message):
    bot.reply_to(message, 'Создатель:\nzzsxd')
    bot.send_message(message.chat.id, 'Введите свой город, чтобы начать!')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        #print(f'{res.json()}')
        bot.reply_to(message, f"🌤Погода🌤\n☀️Сейчас температура: {data['main']['temp']}\n🔥Ощущается как: {data['main']['feels_like']}\n🌨Минимальная температура: {data['main']['temp_min']}\n☀️Максимальная температура: {data['main']['temp_max']}\n💨Скорость ветра: {data['wind']['speed']}м/с")
    else:
        bot.reply_to(message, '🚫Неправильно указан город🚫')


bot.polling(none_stop=True)