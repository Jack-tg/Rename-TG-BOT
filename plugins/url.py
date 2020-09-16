import datetime
import pyrogram 
from pyrogram import Filters,Client




@pyrogram.Client.on_message(Filters.private & ((Filters.text & ~Filters.edited) | Filters.media) & Filters.incoming)
async def _(m):
    
    if m.media:
        if is_valid_file(m):
            return


    snt = await m.reply_text("Hi there, Please wait while I'm getting everything ready to process your request!", quote=True)
    
    
