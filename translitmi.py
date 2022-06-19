import telebot
from transliterate import translit

token = '5579106297:AAF1yXX9OytWQXNF7LMClZO8P8S3li8sz3w'
bot = telebot.TeleBot(token)

# Приветствие при старте
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️, отправь мне текст для транслитирации!")

# проверка на кирилицу
def match(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return not alphabet.isdisjoint(text.lower())

# Ответ на рандомные сообщения | должен быть после команд
@bot.message_handler(content_types=["text"])
def text_message(message):
    texttru = match(message.text)
    if texttru == True:
        bot.send_message(message.chat.id, translit(message.text, reversed=True))
    else:
        bot.send_message(message.chat.id, translit(message.text, 'ru'))


bot.polling(none_stop=True)
