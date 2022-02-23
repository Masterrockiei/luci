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
from config import GROUP_ID
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from youtubesearchpython import SearchVideos
import yt_dlp
from youtube_search import YoutubeSearch
import requests

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

@Client.on_message(filters.command(["song"]) & ~filters.channel & ~filters.edited & filters.chat(GROUP_ID))
def a(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply("**🎵 Processing**")
    ydl_opts = {
        "format": "bestaudio",
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }
        ],
        "outtmpl": "downloads/%(track)s.mp3" ,
    }
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]

            if time_to_seconds(duration) >= 1800:  # duration limit
                 m.edit("Exceeded 30mins cap")
                 return

            performer = f"[Riya Music Bot]" 
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True) 
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit("Server busy due to overload, Please try again later.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ᖇᗴᗩՏOᑎ", callback_data="err_msg")]])))
            return
    except Exception as e:
        m.edit("Use a valid command , /song song name")
        print(str(e))
        return
    m.edit("**⬆️ Uploading**")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict) 
            ydl.process_info(info_dict)
        rep = f"""
♬ <b>Title : {title}</b>
♬ <b>Duration : {duration}</b>
♬ <b>Link : <a href='{link}'>Click here</a></b>
♬ <b>Requested By : {message.from_user.mention}</b>
        """
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(
        audio_file,
        caption=rep,
        parse_mode='HTML',
        quote=False,
        title=title,
        duration=dur,
        performer=performer,
        thumb=thumb_name,
        reply_to_message_id=message.message_id
        )
        m.delete()
    except Exception as e:
        m.edit(
          text='There is an error while processing your request.',
          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ᖇᗴᗩՏOᑎ", callback_data="err_msg")]]))
        print(e)
    try: 
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
        
@Client.on_callback_query(filters.regex("err_msg"))
async def error_msg(bot, query):
    if not query.from_user.id:
      await query.reply("Sorry this isn't for you", show_alert=True)
    else:
      await query.reply("Maybe you entered a wrong song name", show_alert=True)
      return
    

