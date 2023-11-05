import json

import telebot
import requests
from datetime import datetime
from setting import api_t, api_w

bot = telebot.TeleBot(api_t)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет. Напиши название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    try:
        city = message.text.strip().lower()
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_w}&units=metric")
        data = json.loads(res.text)
        bot.reply_to(message, f"Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                          f"Город: {data['name']}\n"
                          f"Сейчас погода: {data['main']['temp']} С\n"
                          f"Влажность: {data['main']['humidity']}%\n"
                          f"Давление: {data['main']['pressure']} рт.ст.\n"
                          f"Скорость ветра: {data['wind']['speed']} м/с")
    except Exception as e:
        bot.reply_to(message, "Введи корректно название города.")


bot.polling(none_stop=True)
