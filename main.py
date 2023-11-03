import telebot
import webbrowser

from setting import api_t, api_w
from telebot import types


bot = telebot.TeleBot(api_t)


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('http://dexycom.ru')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name} {message.from_user.last_name}")


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "Помощь <b><u>спешит</u></b> на помощь", parse_mode='html')


@bot.message_handler(commands=['menu'])
def menu_command(message):
    bot.send_message(message.chat.id, f"/help - Помощь\n/site - Перейти на сайт\n/true - тестовый", parse_mode='html')


@bot.message_handler(commands=['true'])
def crud(message):
    keyboard = types.InlineKeyboardMarkup()
    # вариант когда кнопка друго под другом
    keyboard.add(types.InlineKeyboardButton("Кнопка 1", callback_data='delete'))
    keyboard.add(types.InlineKeyboardButton("Кнопка 2", callback_data='update'))
    # вариант кнопок в одну строку
    button1 = types.InlineKeyboardButton("Button1", callback_data='delete')
    button2 = types.InlineKeyboardButton("Button2", callback_data='update')
    button3 = types.InlineKeyboardButton("Button3", url='http://dexycom.ru')
    keyboard.add(button2, button1, button3)
    # создадим строки кнопок
    button4 = types.InlineKeyboardButton("Button4", callback_data='delete')
    button5 = types.InlineKeyboardButton("Button5", callback_data='update')
    keyboard.row(button4, button5)
    bot.send_message(message.chat.id, "Варианты выбора", reply_markup=keyboard)


# срабатывает при любом вводе текста
@bot.message_handler(content_types=['text'])
def any_text(message):
    keyboard1 = types.InlineKeyboardMarkup()
    # вариант кнопок в одну строку
    button1 = types.InlineKeyboardButton("Button1", callback_data='delete')
    button2 = types.InlineKeyboardButton("Button2", callback_data='update')
    button3 = types.InlineKeyboardButton("Button3", url='http://dexycom.ru')
    keyboard1.add(button2, button1, button3)
    bot.send_message(message.chat.id, "Я не понял тебя, выбери один из вариантов", reply_markup=keyboard1)


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f"Привет {message.from_user.first_name} {message.from_user.last_name}")
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Кнопка1", callback_data='del')
        button2 = types.InlineKeyboardButton("Кнопка2", callback_data='edit')
        button3 = types.InlineKeyboardButton("Кнопка3", callback_data='tols')
        markup.add(button1, button2, button3)
        bot.reply_to(message, 'Выбери один из вариантов кнопок', reply_markup=markup)
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID {message.chat.id}')


# для обработки callback_data создадим обработчик
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message.id)



bot.polling(none_stop=True)

