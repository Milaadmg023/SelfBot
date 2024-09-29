from pyrogram import Client, filters
from pyrogram.types import Message
from modules.db import DB_Controller
from helpers.greeting import greeting
from helpers.quick_replys import quick_reply
from helpers.public_msgs import public_msgs

db = DB_Controller()

@Client.on_message(filters.private & ~filters.me)
async def private_handler(client:Client , message:Message):
    userid = message.from_user.id
    txt = message.text
    await greeting(client, message , userid)
    # handleing quick replys
    if txt == "تست":
        await quick_reply(client, message , txt)
    elif txt == "کارت":
        await quick_reply(client, message , txt)

@Client.on_message(filters.me)
async def me_handler(client:Client , message:Message):
    txt = message.text
    userid = message.chat.id
    if txt == "add":
        await message.delete()
        db.add_customer(userid)
    elif txt == "همگانی":
        await public_msgs(client, message)
    else:
        await quick_reply(client , message , txt)