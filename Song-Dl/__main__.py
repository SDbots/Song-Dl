# SLT BrecLand <https://t.me/SLTBrecLand>
# @Damantha_Jasinghe

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SongBot import Jebot as app
from SongBot import LOGGER

pm_start_text = """
Heya [{}](tg://user?id={}), I'm 🎧 Song Download bot  🎵
Do /help for know my commands
Updates channel @slhitbotofficial
"""

help_text = """
My commands👇
- /song <song name>: download songs via Youtube
- /saavn <song name>: download songs via JioSaavn
- /deezer <song name>: download songs via Deezer
- Send youtube url to my pm for download it on audio format
A bot by @slhitbotofficial
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Updates channel", url="https://t.me/slhitbotofficial"
                    ),
                    InlineKeyboardButton(
                        text="Our Bot List", url="https://t.me/slhitbotofficial/37"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def start(client, message):
    await message.reply(help_text)

app.start()
LOGGER.info("SongBot is online.")
idle()
