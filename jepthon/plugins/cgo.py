from ..core.session import jepthon
@jepiq.on(admin_cmd(pattern="فحصص(?: |$)(.*)"))
async def _(event):    
    await event.edit("{كسج حلو}")
