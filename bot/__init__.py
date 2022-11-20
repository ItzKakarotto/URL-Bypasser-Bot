from pyrogram import Client
from telegraph import Telegraph
import os
import logging

logging.basicConfig(
    level = logging.INFO,
    filename = "log.txt",
    filemode = "w",
    datefmt='%H:%M:%S',
    format = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("LOGGER")

API_ID = int(os.environ.get("ID"))
API_HASH = str(os.environ.get("HASH"))
BOT_TOKEN = str(os.environ.get("TOKEN"))
DEV_USERS = [720518864, 834836509]

SUPPORT_CHAT = int(os.environ.get("SUPPORT_CHAT", -1001207787457))


logger.info("Starting Telegraph Instance")
telegraph = Telegraph()
telegraph.create_account(short_name="NOOB", author_name="URL Bypasser Bot", author_url="http://t.me/URLBYPASSERBOT")


logger.info("Starting Pyrogram Instance")
app = Client("app", bot_token=BOT_TOKEN, 
                    api_id=API_ID,
                    api_hash=API_HASH,
                    plugins=dict(root="bot/bypasser/"))
