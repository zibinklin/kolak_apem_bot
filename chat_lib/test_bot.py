from telegram.ext import Updater
import logging

updater = Updater(token='1470794848:AAGLbv_OxiLNU9WR4XzOcW2KXr3KCSx0PgA',use_context=True)
print(f'value of updater :{updater} ')

dispacher = updater.dispatcher
print(f'value of dispacher : {dispacher}')

logging_value = logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
print(f'value dari logging : {logging_value}')

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
