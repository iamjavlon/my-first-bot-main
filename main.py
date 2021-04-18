from telegram import *
from telegram.ext import *


def start(update, context):
    print(update.message)
    update.message.reply_text('Hello, Javlon!')
    

def main():
    updater = Updater(token='1737438516:AAGj-HbivfGIyz22d-5dZFF-94HEYON1OTA')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()


main()
