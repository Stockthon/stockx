from ..core.session import jepiq
import asyncio
@jepiq.on(admin_cmd(pattern=r"\وعد بخ (.*)"))
async def _(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await jepiq.send_message(chat,'بخشيش')
        await asyncio.sleep(605)
@jepiq.on(admin_cmd(pattern=r"\وعد ر (.*)"))
async def _(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await jepiq.send_message(chat,'راتب')
        await asyncio.sleep(605)
        
#تخمط بدون ماتذكر حقوق انيج اختك 
#RICKTHON
@jepiq.on(admin_cmd(pattern=r"\وعد اس (.*)"))
async def _(event):
        for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
            
            chat = event.chat_id
            await jepiq.send_message(chat, 'فلوسي')
            await asyncio.sleep(0.5)
            masg = await jepiq.get_messages(chat, limit=1)
            masg = masg[0].message
            masg = ("".join(masg.split(maxsplit=2)[2:])).split(" ", 2)
            msg = masg[0]
            if int(msg) > 500000000:
                await jepiq.send_message(chat, f"استثمار {msg}")
                await asyncio.sleep(10)
                mssag2 = await jepiq.get_messages(chat, limit=1)
                await mssag2[0].click(text="اي ✅")
            else:
                await jepiq.send_message(chat, f"استثمار {msg}")
            await asyncio.sleep(1210)
@jepiq.on(events.NewMessage(outgoing= True,pattern=r'^\.تيك'))
async def e(event):
                chat = event.get_chat()
                h = event.text
                mes = h.replace('.تيك ','')
                await event.edit('انتظر...')
                url = f"https://tiktok-best-experience.p.rapidapi.com/user/{mes}"
                headers = {
		"x-rapidapi-key":"d0cbbe1f79mshe3c74080d9d0da5p1de4ddjsn21db44140e77",
		"x-rapidapi-host":"tiktok-best-experience.p.rapidapi.com",
		"User-Agent":"TikTracker/1.2 (com.markuswu.TikTracker; build:1; iOS 14.4.0) Alamofire/5.4.4"
	}
                r = (requests.get(url,headers=headers).json())
                
                if r['status'] == 'ok':
                 
                  insta = ''
                  uid = ''
                  name=''
                  yc=''
                  bio=''
                  h=''
                  fg=''
                  fs=''
                  p= r['data']['avatar_medium']['url_list'][0]
                  try:
                      uid = r["data"]["uid"]
                  except:
                      uid='not found'
                  try:
                      yc = r["data"]["youtube_channel_id"]
                  except:
                      yc='not found'
                  try:
                      h = r["data"]["total_favorited"]
                  except:
                      h='0'
                  try:
                      fg = r["data"]["following_count"]
                  except:
                      fg='0'
                  try:
                      fs = r["data"]["follower_count"]
                  except:
                      fs='0'
                  try:
                      name = r["data"]["nickname"]
                  except:
                      name='not found'
                  try:
                      bio = r["data"]["signature"]
                  except:
                      bio = 'not found'
    
                  try:
                      insta = r["data"]["ins_id"]
                  except:
                      insta = 'not found'
           
                await event.edit(f'''
• Name : {name}

• Followers : {fs}

• Following : {fg}

• Instagram : {insta}

• Youtube Chanel : {yc}

• Likes : {h}

• Bio : {bio}

• iD : {uid}
= = = = = = = = = = = = = = = = = = = = 
By : @P_J_I To : @RICKTHON''')
