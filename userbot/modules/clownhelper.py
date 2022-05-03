""" Userbot module for other small commands. """
from userbot import CMD_HELP, owner, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, clown_cmd


@clown_cmd(pattern="lhelp$")
async def usit(e):
    await edit_or_reply(e,
                        f"**Halo {owner} Jika Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `{cmd}help` Atau Bisa Minta Bantuan Ke:\n"
                        "\n[Telegram](t.me/IamKitaro)"
                        "\n[Repo](https://github.com/JimmyMahendra/Clown-Userbot)"
                        "\n[Instagram](instagram.com/jimmymhndra)")


@clown_cmd(pattern="vars$")
async def var(m):
    await edit_or_reply(m,
                        f"**Disini Daftar Vars Dari {owner}:**\n"
                        "\n[DAFTAR VARS](https://raw.githubusercontent.com/JimmyMahendra/Clown-Userbot/Clown-Userbot/varshelper.txt)")


CMD_HELP.update({
    "helper":
    f"`{cmd}lhelp`\
\nUsage: Bantuan Untuk Clown-Userbot.\
\n`{cmd}vars`\
\nUsage: Melihat Daftar Vars."
})
