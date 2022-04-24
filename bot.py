import os
from pyrogram import Client
from config import API_HASH, API_ID, BOT_TOKEN
pbot = Client(
  "SophieMusicBot",
  API_ID,
  API_HASH,
  bot_token=BOT_TOKEN,
  plugins=dict(root="plugins")
)

pbot.run()
print("Bot has been started")
