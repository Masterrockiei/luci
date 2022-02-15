from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



@Client.on_message(filters.command("start", "find"))
async def start(bot, message):
  m=await message.reply_text("◈◇◇")
  n=await m.edit("◈◈◇")
  p=await n.edit("◈◈◈")
  await p.edit(
    text=f"Hey {message.from_user.mention} ✨,\n\n I am an advanced music bot made for **Kerala Music Hub**"
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("🍂 Group", url="https://t.me/KeralaMuiscHubRedirect"),
        InlineKeyboardButton("🗑️ Close", callback_data="close")
      ]]
    )
  )
  
@Client.on_callback_query(filters.regex("close"))
async def close(bot, message):
  await message.delete()
