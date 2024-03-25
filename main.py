import telebot
from telebot import types
import pyjokes
from googletrans import Translator

bot = telebot.TeleBot("6704785933:AAFy0fsiQmHNvBT5qQbK-kycvQQSmJJLUsA")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Расскажи аненкдот', callback_data='jockets')
    keyboard.add(key_yes)
    bot.send_message(message.from_user.id ,"Привет", reply_markup=keyboard)
translator = Translator()
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "jockets":
        joke = pyjokes.get_joke()
        a = translator.translate(joke, dest='ru')
        print(a)
        print(joke)
bot.polling(non_stop=True)