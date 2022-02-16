import os
from pyrogram import Client

pbot = Client(
  "Music Bot",
  api_hash=os.environ.get("API_HASH"),
  api_id=int(os.environ.get("API_ID")),
  bot_token=os.environ.get("BOT_TOKEN"),
  plugins=dict(root="plugins")
)

pbot.run()
print("Bot has been started")
