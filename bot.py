import os
from pyrogram import Client
from config import Config
pbot = Client(
  Config.SESSION_NAME,
  Config.API_HASH,
  Config.API_ID,
  bot_token=Config.BOT_TOKEN,
  plugins=dict(root="plugins")
)

pbot.run()
print("Bot has been started")
