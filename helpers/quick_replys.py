from pyrogram import Client
from pyrogram.types import Message
from modules.db import DB_Controller
import config

chat_id = config.CHANNEL
test_id = config.TEST
card_id = config.CARD
ONE_TIME_TXT = config.ONE_TIME_TXT
QUICK_TXT = config.QUICK_TXT

db = DB_Controller()


async def quick_reply(client: Client, message: Message, txt):
    userid = message.from_user.id
    if txt == ONE_TIME_TXT:
        if db.handle_test(userid):
            await client.copy_message(chat_id=message.chat.id, from_chat_id=chat_id, message_id=test_id)
        else:
            await message.reply(f"شما قبلا {ONE_TIME_TXT} دریافت کرده اید.")
    elif txt == QUICK_TXT:
        await client.copy_message(chat_id=message.chat.id, from_chat_id=chat_id, message_id=card_id)