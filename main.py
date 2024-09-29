import logging
from pyrogram import Client
import config

LOGGER = logging.getLogger(__name__)

API_ID = config.API_ID
API_HASH = config.API_HASH

PLUGINS = dict(root="plugins")

app = Client(
    "selfbot",
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=PLUGINS
)

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()