from JE313P import JE313P, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
Hello.My Bro ! {}

I m a telegram streaming bot with some useful features. Supporting platforms like Youtube, Spotify, Resso, AppleMusic , Soundcloud etc.

Feel free to add me to your groups.
γππΎπππ²π΄ π΄ππ°π»π΄π΄γ(@E4V4ER)
"""

@JE313P.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("β Add me to your Group", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("π¨ Source", "https://t.me/E4V4ER")],
        [Button.url("π¨ Support", f"https://t.me/{Config.SUPPORT}"), Button.url("π¨ Channel", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("π How to Use? Commands Meun.", data="help")]])
       return

    if event.is_group:
       await event.reply("**- Ψ§ΩΩΨ§ Ψ¨Ω Ψ§ΩΨ§ Ψ§ΨΉΩΩ Ψ¨ΩΨ¬Ψ§Ψ­**")
       return



@JE313P.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("β Add me to your Group", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("π¨ Source", "https://t.me/E4V4ER")],
        [Button.url("π¨ Support", f"https://t.me/{Config.SUPPORT}"), Button.url("π¨ Channel", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("π How to Use? Commands Meun.", data="help")]])
       return
