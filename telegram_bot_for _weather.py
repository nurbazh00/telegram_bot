import requests
import telebot
import os

url = 'http://api.openweathermap.org/data/2.5/weather'
api_weather = os.getenv('API_WEATHER')
token = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, f'Добро пожаловать!   {message.from_user.first_name} \n'
                                      f'Что бы узнать погоду напишите названия города')


@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id,
                     '/start запуск бота\n Что бы узнать погоду напишите названия города')


@bot.message_handler(content_types=['text'])
def test(message):
    city_name = message.text

    try:
        params = {'APPID': api_weather, 'q': city_name, 'units': 'metric', 'lang': 'ru'}
        result = requests.get(url, params=params)
        weather = result.json()

        if weather["main"]['temp'] < 10:
            status = "Одевайтесь тепло, на улице холодно!"
        elif weather["main"]['temp'] < 15:
            status = "Одевайтесь потеплее, на улице прохладно!"
        elif weather["main"]['temp'] < 21:
            status = "На улице тепло, идеальная погода чтобы гулять!"
        elif weather["main"]['temp'] < 27:
            status = "Пейте много воды, на улице жарко!"
        else:
            status = "Не выходите на улицу без надобности и пейте много воды, на улице жарко!"

        bot.send_message(message.chat.id, "Сейчас в городе " + str(weather["name"]) + " температура " +
                         str(weather["main"]['temp']) + "°C" + "\n" +
                         "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "На улице сейчас " + str(weather['weather'][0]["description"]) + "\n" 
                         "-------------------------------------------------------------------"
                         "\n" + status)

    except:
        bot.send_message(message.chat.id, "Город " + city_name + " не найден")


bot.polling()