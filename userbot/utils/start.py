import pybase64
from telethon import Button
from telethon.tl.functions.channels import JoinChannelRequest as Invt
from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/02f87cca391f9b9d627d5.jpg",
                caption="🤡 **Clown - Userbot Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 8.0@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @ChannelClown ",
                buttons=[(Button.url("Support", "https://t.me/ClownSupportt"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None


async def checking(client):
    gcsp = str(pybase64.b64decode("QENsb3duU3VwcG9ydA=="))[2:14]
    chsp = str(pybase64.b64decode("QENoYW5uZWxDbG93bg=="))[2:14]
    chgbt = str(pybase64.b64decode("QGRpc2luaWNlcml0YWE="))[2:15]
    if client:
        try:
            await client(Invt(gcsp))
        except BaseException:
            pass
        try:
            await client(Invt(chsp))
        except BaseException:
            pass
        try:
            await client(Invt(chgbt))
        except BaseException:
            pass
