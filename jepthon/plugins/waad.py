from ..core.session import jepiq

@jepiq.on(admin_cmd(pattern=r"\.ر وعد (.*)"))

async def _(event):    

    await event.edit("دبلع")
