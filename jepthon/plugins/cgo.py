from ..core.session import jepiq
@jepiq.on(admin_cmd(pattern=r"\.وعد ر (.*)"))
async def _(event):    
    await event.edit("{كسج حلو}")
