import telebot
from telebot import types


bot = telebot.TeleBot('7521702710:AAElwFPr8VSeU2ipuQILC6X2UBdMd9_CwrE')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    rentMotoBtn = types.KeyboardButton('Аренда мотоциклов')
    markup.row(rentMotoBtn)
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}. Чем могу помочь?', reply_markup=markup)


bot.polling(none_stop=True)