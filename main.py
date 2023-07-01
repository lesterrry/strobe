import os.path
import yaml
from telethon import TelegramClient, events, sync, functions, types

EXEC_PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE_PATH = f'{EXEC_PATH}/config.yaml'
CONFIG = None

with open(CONFIG_FILE_PATH, 'r') as file:
	CONFIG = yaml.safe_load(file)

async def get_chats() -> None:
	async for i in client.iter_dialogs():
		print(i)

client = TelegramClient(f'{EXEC_PATH}/strobe.session', CONFIG['api_id'], CONFIG['api_hash'])
client.start()

result = client(functions.account.UpdateEmojiStatusRequest(
	emoji_status = types.EmojiStatus(
		document_id = 5454327849936755071  # Replace with your emoji's document_id
	)
))
