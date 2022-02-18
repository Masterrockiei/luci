from __future__ import unicode_literals
import asyncio
import math
import os
import time
import ffmpeg
import aiofiles
import aiohttp
import wget
from pyrogram import Client, filters
from config import Config
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from youtubesearchpython import SearchVideos
import yt_dlp
from youtube_search import YoutubeSearch
import requests

def time_second(time):
	string = str(time)
	return sum(int(x) * 60 ** i for i, x in enumerate(reversed(string.split(":"))))
	
@Client.on_message(filters.command(["song"]) & ~filters.chanel & ~filters.edited & filters.chat(Config.GROUP_ID))
async def music(client, message):
  global is_downloading
  if is_downloading:
    await message.reply_text("Please wait an another download is on process")
    return
  is_downloading = True
  query = ''
  for i in message.command[1:]:
    query += ' ' + str(i)
  print(query)
  m = await message.reply_text("🎵 Processing")
  ydl_opts = {
    "format" : "bestaudio",
    "key" : "FFmpegMetadata",
    "prefer_ffmpeg" : True,
    "postprocessors" : [
      {
        "key" : "FFmpegExtractAudio",
        "preferredcodec" : "mp3",
        "preferredquality" : "320",
      }
    ],
    "outtmpl" : "downloads/%(track)s.mp3",
  }
  try:
    results = []
    count = 0
    while len(results) == 0 and count < 6:
      if count>0:
        time.sleep(1)
      results = YoutubeSearch(query, max_results=1).to_dict()
      count += 1
    try:
      link = f"https://youtube.com{results[0]['url_suffix']}"
      title = result[0]['title']
      dur = results[0]['duration']
      thumbs = results[0]['thumbnails']
      
      if time_second(dur) >= 900:
        await m.edit("The video duration is more than 15 minutes")
        return

      performer = f"[RiyaMusicBot]"
      thumb_name = f'thumb{message.message_id}.jpg'
      thumb = request.get(thumbs, allow_redirects=True)
      open(thumb_name, 'wb').write(thumb.content)
      
    except Exception as e:
      print(e)
      await m.edit("**Server busy due to overload in server**")
      return
  except Exception as e:
    await m.edit(f"Sorry i can't find any song for your {query} ")
    print(str(e))
    return
  await m.edit("**⬆️ Uploading**")
  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      info_dict = ydl.extract_info(link, download=False)
      audio_file = ydl.prepare_filename(info_dict)
      ydl.process_info(info_dict)
      rep = f""" 
♬ <b>Title : {title}</b>\n
♬ <b>Duration : {dur}</b>  
♬ <b>Link : <a href='{link}'>Click here</a></b>\n
♬ <b>Requested By : {message.from_user.mention}</b>
      """
      secmul, durs, dur_arr = 1, 0, dur.split(':')
      for i in range(len(dur_arr)-1, -1, -1):
        durs += (int(dur_arr[i]) * secmul)
        secmul *= 60
      await message.reply_audio(
        audio_file,
        caption=rep,
        parse_mode='html',
        qoute=True,
        title=title,
        dur=durs,
        performer=performer,
        thumb=thumb_name,
        reply_to_message_id=message.message_id
        ),
  await m.delete()
  except Exception as e:
    await m.edit("There is an error with your download request.")
    print(e)
  try:
    if not os.path.exist(FilePath):
      await message.reply_audio(audio_file)
      os.remove(thum_name)
  except Exception as e:
    print(e)
    
  is_downloading = False
