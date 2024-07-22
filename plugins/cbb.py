#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>ᴀᴅᴍɪɴ ʙᴏᴛ : <a href='tg://user?id={OWNER_ID}'>𝑚𝑎𝑑𝑎𝑟𝑎</a>\n○ ᴀᴅᴍɪɴ ᴠɪᴘ : <a href='https://t.me/tyaa86'>ɴᴏᴠɪᴧ8̷6̷.</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ɢʀᴜᴘ ᴠɪᴘ', url='https://t.me/rajakonten_testi/83')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass


