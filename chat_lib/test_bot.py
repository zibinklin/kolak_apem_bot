from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from telegram import files
import sys
from telegram import Bot
import logging

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.effective_chat.id)

def message(update,context):
    update.message.reply_text(update.message.text)

def command_handler(update,contex):
    update.message.reply_text(f'mendeteksi bahwa {update.message.text} adalah command')

def main():
    updater = Updater(token='1470794848:AAGLbv_OxiLNU9WR4XzOcW2KXr3KCSx0PgA',use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(MessageHandler(Filters.text,message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
   main()
