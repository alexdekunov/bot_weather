import telebot
import webbrowser

from setting import api_t, api_w


bot = telebot.TeleBot(api_t)


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('http://dexycom.ru')



@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name} {message.from_user.last_name}")


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, "Помощь <b><u>спешит</u></b> на помощь", parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f"Привет {message.from_user.first_name} {message.from_user.last_name}")
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID {message.chat.id}')


bot.polling(none_stop=True)

