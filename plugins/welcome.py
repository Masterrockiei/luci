import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, User



@Client.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
	m=await bot.send_message(text=f"Welcome {message.from_user.mention} to {message.chat.title},  Happy to see you here",chat_id=chatid)
	await asyncio.sleep(6)
	await m.delete()
   
@Client.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	n=await bot.send_message(text=f"Bye ,  {message.from_user.mention} , Have a Nice Day",chat_id=chatid)
	await asyncio.sleep(6)
	await n.delete()
	
	
