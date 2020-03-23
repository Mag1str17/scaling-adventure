import pyowm
import telebot

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

owm = pyowm.OWM('554698e963b6d5136fa3c8ef159a0408', language = "ua")
bot = telebot.TeleBot("1115856048:AAFmjzqDtZbT18bRF2ib2m6KAbIm8HypPgU")

@bot.message_handler(commands=['start'])
def send_welcome(message):
		bot.send_message(message.chat.id, "Привіт, в якому місті будемо дивитись погоду?")

@bot.message_handler(commands=['help'])
def send_welcome(message):
		bot.send_message(message.chat.id, "Бот для погоди")


@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]
	speed = w.get_wind()["speed"]
	hum = w.get_humidity()
	

	answer = "В місті " + message.text + " зараз " + w.get_detailed_status() + "\n"
	answer += "Температура зараз в районі " + str(temp) + "°" + "\n"
	answer += "Швидкість вітру " + str(speed) + " м/cек" + "\n"
	answer += "Вологість " + str(hum) + " %" + "\n\n"
	
	if temp < 10:
		answer += "Холоднувато!"
	bot.send_message(message.chat.id, answer)

	speed = w.get_wind()["speed"]
	anspeed = "Швидкість вітру" + str(speed) 

bot.polling( none_stop = True )