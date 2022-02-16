import os
from json import JSONDecodeError

import requests

# import ffmpeg
from pyrogram import filters
from plugins.function.pluginhelpers import edit_or_reply, fetch_audio
from pyrogram import Client


@Client.on_message(filters.command(["find", "identify"]))
async def shazamm(client, message):
    kek = await edit_or_reply(message, "Identifying the song !!")
    if not message.reply_to_message:
        await kek.edit("Reply To The Audio.")
        return
    if os.path.exists("riya.mp3"):
        os.remove("riya.mp3")
    kkk = await fetch_audio(client, message)
    downloaded_file_name = kkk
    f = {"file": (downloaded_file_name, open(downloaded_file_name, "rb"))}
    await kek.edit("**Searching For This Song In RiyaMusicBot DataBase.**")
    r = requests.post("https://starkapi.herokuapp.com/shazam/", files=f)
    try:
        xo = r.json()
    except JSONDecodeError:
        await kek.edit(
            "`Seems Like Our Server Has Some Issues, Please Try Again Later!`"
        )
        return
    if xo.get("success") is False:
        await kek.edit("`Song Not Found IN Database. Please Try Again.`")
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
    messageo = f"""<b>Song Shazamed.</b>
<b>Song Name : </b>{title}
<b>Song By : </b>{by}
<u><b>Identified using Riya Music Bot ~ @RiyaMusicBot </b></u>
<i>Powered By AI</i>
"""
    await client.send_photo(message.chat.id, image, messageo, parse_mode="HTML")
    os.remove(downloaded_file_name)
    await kek.delete()



