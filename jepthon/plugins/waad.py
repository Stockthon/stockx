from jepthon import jepiq
import telethon
import asyncio
@jepiq.on(admin_cmd(pattern=r".اه"))
async def _(event):
    
        chat = event.chat_id
        await jepiq.send_message(chat,'اه')
        
