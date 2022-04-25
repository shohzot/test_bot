from telegram import *
import api
from telegram.ext import *
from pymongo import MongoClient
import response


print("Bot started...")

#   -----  This is help command    -------
def help_command(update, context):
    update.message.reply_text('Iltimos /start ni bosing!')

#       ------  Error handler  ---------------
def error(update, context):
    print(f"Update {update} caused error {context.error}")



def main():
    updater = Updater(api.API, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('start', response.startCommand))
    dp.add_handler(MessageHandler(Filters.text, response.message_handler))
    dp.add_handler(CallbackQueryHandler(response.button))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()


