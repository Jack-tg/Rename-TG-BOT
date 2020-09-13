import datetime

from pyrogram import filters as  Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..utils import is_url, is_valid_file, get_duration, gen_ik_buttons, generate_stream_link
from ..screenshotbot import ScreenShotBot
from ..config import Config


@ScreenShotBot.on_message(Filters.private & ((Filters.text & ~Filters.edited) | Filters.media) & Filters.incoming)
async def _(c, m):
    
    if m.media:
        if not is_valid_file(m):
            return
    else:
        if not is_url(m.text):
            return

    snt = await m.reply_text("Hi there, Please wait while I'm getting everything ready to process your request!", quote=True)
    
