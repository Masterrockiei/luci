import asyncio
from time import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import Config

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

@Client.on_message(filters.command(["start", "find"]) & filters.chat(Config.GROUP_ID) | filters.private)
async def start(bot, message):
  current_time = datetime.utcnow()
  uptime_sec = (current_time - START_TIME).total_seconds()
  uptime = _human_time_duration(int(uptime_sec))
  m=await message.reply_text("◈◇◇")
  n=await m.edit("◈◈◇")
  p=await n.edit("◈◈◈")
  await p.edit(
    text=f"**Hey {message.from_user.mention} ✨**,\n\nMy Name Is **Riya** I'm An **Advanced** Music Bot Specially Made For **Kerala Music Hub**\n\n**Bot Uptime : {uptime}**",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("🍂 ᘜᖇOᑌᑭ", url="https://t.me/KeralaMusicHubRedirect"),
        InlineKeyboardButton("☘️ Oᗯᑎᗴᖇ", url="https://t.me/PaulWalker_TG")
     ],[
        InlineKeyboardButton("🗑️ ᑕᒪOՏᗴ", callback_data="close")
      ]]
    )
  )
  
@Client.on_callback_query(filters.regex("close"))
async def close(bot, query):
  await query.message.delete()


def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@Client.on_message(filters.text
                   & (filters.chat(Config.GROUP_ID) | filters.user(Config.ADMINS))
                   & filters.incoming
                   & ~filters.edited
                   & filters.regex("^uptime$"))
async def get_uptime(_, message: Message):
    """/uptime Reply with readable uptime and ISO 8601 start time"""
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = _human_time_duration(int(uptime_sec))
    reply = await message.reply_text(f"**Uptime:** `{uptime}`\n"
                                     f"**Start time:** `{START_TIME_ISO}`",
                                     quote=True)

