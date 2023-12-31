import telebot
from telebot import types

TOKEN = '5769907387:AAF0tVVa2RNQjFpOeYmRAIWBhzIBa1jFp4E'
bot = telebot.TeleBot(TOKEN)

# Define your bot handlers as usual
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello!")

# The Lambda function handler
def handler(event, context):
    json_str = event['body']
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return {'statusCode': 200, 'body': ''}
