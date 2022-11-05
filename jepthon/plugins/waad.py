from ..core.session import jepiq as huks
import asyncio
@huks.on(admin_cmd(pattern=r"\.بخ رعد (.*)"))
async def _(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await huks.send_message(chat,'بخشيش')
        await asyncio.sleep(605)
@huks.on(admin_cmd(pattern=r"\.ر وعد (.*)"))
async def _(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await huks.send_message(chat,'راتب')
        await asyncio.sleep(605)
        
@huks.on(admin_cmd(pattern=r"\.اس وعد (.*)"))
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
