import datetime
import pyrogram 
from pyrogram import Filters,Client




@pyrogram.Client.on_message(Filters.private & ((Filters.text & ~Filters.edited) | Filters.media) & Filters.incoming)
async def _(c, m):
    
    if m.media:
        if not is_valid_file(m):
            return
    else:
        if not is_url(m.text):
            return

    snt = await m.reply_text("Hi there, Please wait while I'm getting everything ready to process your request!", quote=True)
    
    
