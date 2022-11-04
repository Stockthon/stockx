from jepthon import jepiq as huks
import telethon
from telethon.tl.functions.messages import ImportChatInviteRequest
from core session import *
from telethon import events
import asyncio



@huks.ar_cmd(pattern=r"\.بخشيش وعد (.*)")
async def _(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await huks.send_message(chat,'بخشيش')
        await asyncio.sleep(605)
@jepiq.ar_cmd(pattern=r"\.راتب وعد (.*)")
async def _(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await huks.send_message(chat,'راتب')
        await asyncio.sleep(605)
       
@huks.ar_cmd(pattern=r"\.استثمار وعد (.*)")
async def _(event):
        for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
            
            chat = event.chat_id
            await huks.send_message(chat, 'فلوسي')
            await asyncio.sleep(0.5)
            masg = await huks.get_messages(chat, limit=1)
            masg = masg[0].message
            masg = ("".join(masg.split(maxsplit=2)[2:])).split(" ", 2)
            msg = masg[0]
            if int(msg) > 500000000:
                await huks.send_message(chat, f"استثمار {msg}")
                await asyncio.sleep(10)
                mssag2 = await huks.get_messages(chat, limit=1)
                await mssag2[0].click(text="اي ✅")
            else:
                await huks.send_message(chat, f"استثمار {msg}")
            await asyncio.sleep(1210)
