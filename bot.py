import os
from pyrogram import Client

Client = Client(
  "Music Bot",
  api_hash=os.environ.get("API_HASH"),
  api_id=int(os.environ.get("API_ID")),
  bot_token=os.environ.get("BOT_TOKEN"),
  plugins=dict(root="plugins")
)

Client.run()
print("Bot has been started")
