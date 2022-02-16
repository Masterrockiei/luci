import asyncio
from shazamAPI import Shazam
from pyrogram import Client, filters

Pack = filters.audio | filters.music | filters.video

@Client.on_message(filters.comand("find") & Pack)
async def main(bot, message):
  mp3_file_content_to_recognize = open('a.mp3', 'rb').read()
  shazam = Shazam(mp3_file_content_to_recognize)
  recognize_generator = shazam.recognizeSong()
  while True:
    await message.reply_text(f"{recognize_generator}")
  
