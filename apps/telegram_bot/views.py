from django.shortcuts import render
from telebot import TeleBot, types

from .models import TelegramUsers

# Create your views here.

token = "6774314746:AAEgwNioDtJimhkmm4tveqMPZSw2q7GEwBk"
admin_id = 1904375259

bot = TeleBot(token, threaded=False)

@bot.message_handler(commands=['start'])
def start(message:types.Message):
    TelegramUsers.objects.get_or_create(username = message.from_user.username, fullname = message.from_user.full_name)
    bot.send_message(message.chat.id, "привет")

def send_message(message):
    bot.send_message(admin_id, message)