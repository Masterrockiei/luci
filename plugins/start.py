from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import Config


@Client.on_message(filters.command(["start", "find"]) & filters.chat(Config.GROUP_ID))
async def start(bot, message):
  m=await message.reply_text("◈◇◇")
  n=await m.edit("◈◈◇")
  p=await n.edit("◈◈◈")
  await p.edit(
    text=f"**Hey {message.from_user.mention} ✨**,\n\nMy Name Is **Riya** I'm An **Advanced** Music Bot Specially Made For **Kerala Music Hub**",
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



