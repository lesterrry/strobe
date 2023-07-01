import os.path
import yaml
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

EXEC_PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE_PATH = f'{EXEC_PATH}/config.yaml'
CONFIG = None

with open(CONFIG_FILE_PATH, 'r') as file:
    CONFIG = yaml.safe_load(file)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

updater = Updater(token=CONFIG['bot_token'], use_context=True)

dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I want custom emoji!")

def echo(update: Update, context: CallbackContext):
    message = update.message
    for entity in message.entities:
        if entity.type == "custom_emoji":
            emoji_id = entity
            for attribute_name in dir(entity):
                attribute_value = getattr(entity, attribute_name)
                print(f"{attribute_name}: {attribute_value}")
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"Emoji ID: {entity.custom_emoji_id}")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
