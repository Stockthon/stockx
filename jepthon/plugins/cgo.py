from ..core.session import jepiq
@jepiq.on(admin_cmd(pattern="فحصص(?: |$)(.*)"))
async def _(event):    
    await event.edit("{كسج حلو}")
