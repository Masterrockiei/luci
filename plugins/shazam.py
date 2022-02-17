## Commands --------------------------------
from __future__ import unicode_literals
import math
import asyncio
import time
import aiofiles
import aiohttp
import wget
import os
from json import JSONDecodeError
import requests
import ffmpeg
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from youtubesearchpython import VideosSearch
import yt_dlp
from youtube_search import YoutubeSearch
import requests
from pyrogram import filters
from plugins.function.pluginhelpers import edit_or_reply, fetch_audio
from pyrogram import Client


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))



@Client.on_message(filters.command(["find", "identify"]))
async def shazamm(client: Client, message: Message):
    kek = await edit_or_reply(message, "🎧 Listening")
    if not message.reply_to_message:
        await kek.edit("Reply To The Audio.")
        return
    if os.path.exists("riya.mp3"):
        os.remove("riya.mp3")
    kkk = await fetch_audio(client, message)
    downloaded_file_name = kkk
    f = {"file": (downloaded_file_name, open(downloaded_file_name, "rb"))}
    await kek.edit("**@RiyaMusicBot is shazaming ⚡**")
    r = requests.post("https://starkapi.herokuapp.com/shazam/", files=f)
    try:
        xo = r.json()
    except JSONDecodeError:
        await kek.edit(
            "`Seems Like Our Server Has Some Issues, Please Try Again Later!`"
        )
        return
    if xo.get("success") is False:
        await kek.edit("Song not found !!. Please Try Again.")
        os.remove(downloaded_file_name)
        return
    xoo = xo.get("response")
    zz = xoo[1]
    zzz = zz.get("track")
    zzz.get("sections")[3]
    nt = zzz.get("images")
    image = nt.get("coverarthq")
    by = zzz.get("subtitle")
    title = zzz.get("title")
    text = f"""<b>Song Shazamed.</b>
<b>Song Name : </b>{title}
<b>Song By : </b>{by}
<u><b>Identified by @RiyaMusicBot</u></b>
"""
   #  kk = await client.send_photo(message.chat.id, image, text, parse_mode="HTML")
   # os.remove(downloaded_file_name)
   # await kek.delete()

    hm = await kk.reply_text(f"⬆️ Uploading", parse_mode='html')

    yt_result = VideosSearch(
        query=title,
        limit=1,
        region='IN'
    ).result()['result'][0]

    opts = {
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
        with yt_dlp.YoutubeDL(opts) as dl:
            info = dl.extract_info(yt_result['link'], download=False)
            file = dl.prepare_filename(info)
            dl.process_info(info)

        min, sec = yt_result['duration'].split(':',1)
        dur = int(min)*60 + int(sec)

        thumb_res = requests.get(yt_result['richThumbnail']['url'])
        thumb_file = f"{yt_result['title']}.jpg"
        with open(thumb_file, 'wb') as thumb:
            thumb.write(thumb_res.content)

        capt = f"""
        🎵 Song : <code>{yt_result['title']}</code>
        🎵 Requested by : {message.from_user.mention}
        🎵 Duration : {yt_result['duration']}
        """

        await message.reply_audio(
            audio=file,
            caption=capt,
            quote=True,
            parse_mode='html',
            duration=dur,
            performer=f"RiyaMusicBot",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Watch Video", url=yt_result['link'])]]),
            thumb=thumb_file
        )

    except Exception as e:
        print(e)
        await message.reply_text("Sorry Download Failed.")
