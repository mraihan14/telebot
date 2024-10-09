import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token.
TOKEN = '6731749628:AAGPwkR4t2_zjcf5rsUfIJDTjs_Uh5N3THo'
bot = telebot.TeleBot(TOKEN)

# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your bot. How can I assist you?")

# Handle the /help command
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "You can use the following commands:\n/start - Start the bot\n/help - Get help")

# Handle all other text messages (echo)
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# Start polling to listen for new messages
if __name__ == '__main__':
    print('Bot is running...')
    bot.infinity_polling()
