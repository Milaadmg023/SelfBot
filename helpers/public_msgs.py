from pyrogram import Client
from pyrogram.types import Message
from modules.db import DB_Controller
import config


db = DB_Controller()


chat_id = config.CHANNEL
msg_id = config.PUBLIC_MSG

async def public_msgs(client: Client, message: Message):
    customers = db.get_customers()
    for user_id in customers:
        await client.copy_message(chat_id=user_id[0], from_chat_id=chat_id, message_id=msg_id)