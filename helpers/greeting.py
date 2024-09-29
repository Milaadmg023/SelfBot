from modules.db import DB_Controller
from pyrogram import Client
from pyrogram.types import Message
import config
GREETING = config.GREETINGS
CHANNEL_ID = config.CHANNEL

db = DB_Controller()


async def greeting(client: Client, message: Message, user_id):
    if db.handle_user(user_id):
        await client.copy_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=GREETING)
