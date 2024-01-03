import telebot
from telebot import types

# Укажите ваш токен, полученный от BotFather
TOKEN = '6698149570:AAGI8wA3jQYT6Bc2HpXxOXoHtvrm-YPFDl0'

# Создание объекта бота
bot = telebot.TeleBot(TOKEN)

# Словарь с эмоциями и их смайликами
emojis = {
    "Счастье": "😄 😃 😀 😁 😆 😊",
    "Грусть": "😔 😞 😢 😭",
    "Злость": "😡 😠 😤",
    "Удивление": "😲 😯 😦 😧 😮",
    "Любовь": "😍 😘 😚 😻 💖"
}

# Обработчик команды /start или /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    emotions = list(emojis.keys())
    buttons = [types.KeyboardButton(emotion) for emotion in emotions]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Привет! Выбери эмоцию:", reply_markup=markup)

# Обработчик нажатий на кнопки с эмоциями
@bot.message_handler(func=lambda message: True)
def send_emojis(message):
    chat_id = message.chat.id
    if message.text in emojis:
        bot.send_message(chat_id, f"Вот смайлики для эмоции '{message.text}':\n{emojis[message.text]}")
    else:
        bot.send_message(chat_id, "Пожалуйста, выбери эмоцию из списка кнопок.")

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)