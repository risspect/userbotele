# Lord-Userbot
from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(117)

    input_str = event.pattern_match.group(1)

    if input_str == "bulan":

        await event.edit(input_str)

        animation_chars = [
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            f"🌖"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 32])


@register(outgoing=True, pattern='^.heli(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("▬▬▬.◙.▬▬▬ \n"
                     "═▂▄▄▓▄▄▂ \n"
                     "◢◤ █▀▀████▄▄▄▄◢◤ \n"
                     "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
                     "◥█████◤ \n"
                     "══╩══╩══ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ Hallo ANAK STRESS,AKU DATANG :) \n"
                     "╬═╬☻/ \n"
                     "╬═╬/▌ \n"
                     "╬═╬/ \\ \n")



@register(outgoing=True, pattern='^.tembak(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("_/﹋\\_\n"
                     "(҂`_´)\n"
                     "<,︻╦╤─ ҉\n"
                     r"_/﹋\_"
                     "\n**Mau Jadi Pacarku Gak?!**")


@register(outgoing=True, pattern='^.bundir(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`DIDUGA BUNDIR KARNA DI GHOSTING...`          \n　　　　　|"
                     "\n　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　／￣￣＼| \n"
                     "＜ ´･ 　　 |＼ \n"
                     "　|　３　 | 丶＼ \n"
                     "＜ 、･　　|　　＼ \n"
                     "　＼＿＿／∪ _ ∪) \n"
                     "　　　　　 Ｕ Ｕ\n")
                     

@register(outgoing=True, pattern='^.tawa(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("────██──────▀▀▀██\n"
                     "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
                     "▄▀──█▄▄──────█─█▄▄\n"
                     "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
                     "─▀───────▀▀─▀───────▀▀\n`Awkwokwokwok Dasar Stress..`")


@register(outgoing=True, pattern='^.ular(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("░░░░▓\n"
                     "░░░▓▓\n"
                     "░░█▓▓█\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓███\n"
                     "░░░░██▓▓████\n"
                     "░░░░░██▓▓█████\n"
                     "░░░░░░██▓▓██████\n"
                     "░░░░░░███▓▓███████\n"
                     "░░░░░████▓▓████████\n"
                     "░░░░█████▓▓█████████\n"
                     "░░░█████░░░█████●███\n"
                     "░░████░░░░░░░███████\n"
                     "░░███░░░░░░░░░██████\n"
                     "░░██░░░░░░░░░░░████\n"
                     "░░░░░░░░░░░░░░░░███\n"
                     "░░░░░░░░░░░░░░░░░░░\n")


@register(outgoing=True, pattern='^.y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
                     "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
                     "██████▄▄█‡‡‡‡‡‡████████▄\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
                     "█████‡‡‡‡‡‡‡██████████\n")


@register(outgoing=True, pattern='^.tank(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
                     "▂▄▅█████████▅▄▃▂…\n"
                     "[███████████████████]\n"
                     "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n")


@register(outgoing=True, pattern='^.babi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("┈┈┏━╮╭━┓┈╭━━━━╮\n"
                     "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
                     "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
                     "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
                     "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
                     "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
                     "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
                     "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")


@register(outgoing=True, pattern='^.ajg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("╥━━━━━━━━╭━━╮━━┳\n"
                     "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
                     "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
                     "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
                     "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
                     "╨━━┗┛┗┛━━┗┛┗┛━━┻\n")


@register(outgoing=True, pattern='^.gbn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Memulai global banned...✅`")
    sleep(2)
    await typew.edit("`Proses Global banned...✅`")
    sleep(1)
    await typew.edit("♛Perintah : `Tuan Ku`\n"
                     "✣Pengguna :**Jamet Tolol!\n**"
                     "✣Aksi     :`Global banned!`")

@register(outgoing=True, pattern='^.gmt(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Memulai proses Global mute...`")
    sleep(3)
    await typew.edit("`Pengguna berhasil di Global mute bosss...!`")


@register(outgoing=True, pattern='^.tolol(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`TOLOL...`")
    sleep(2)
    await typew.edit("`Pertama Kamu tolol....`")
    sleep(1)
    await typew.edit("`Kedua Kamu memang tolol...`")
    sleep(1)
    await typew.edit("`Ketiga Kamu benar benar tolol..`")
    sleep(1)
    await typew.edit("`Dan kamu di lahirkan Dalam keadaan tolol...`")
    sleep(1)
    await typew.edit("`Dasar kamu anak TOLOL...`")
    sleep(1)
    await typew.edit("`T`")
    await typew.edit("`TO`")
    await typew.edit("`TOL`")
    await typew.edit("`TOLO`")
    await typew.edit("`TOLOL`")
    await typew.edit("`TOLOL!!!!`")

@register(outgoing=True, pattern='^.uasu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Memeriksa dyno heroku anda...`")
    sleep(1)
    await typew.edit("**STRESS USAGE:**\n"
                     "╔════════════════════╗\n"
                     "`✥Penggunaan dyno Anda:`\n"
                     "**❉1000 Jam - 1000 Menit 100%**\n"
                     " ✤⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉✤\n"
                     "✥ `Sisa dyno bulan ini:`\n"
                     "**999999 jam - 999999 Menit 999%**\n"
                     "╚════════════════════╝")

@register(outgoing=True, pattern='^.oy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Woi....**")
    sleep(3)
    await typew.edit("**Grup banyak anggota yakan**")
    sleep(1)
    await typew.edit("**Tapi ga ada yg nimbrung..**")
    sleep(1)
    await typew.edit("**Kan tolol bgt, Jadi sepi kan**")
    sleep(1)
    await typew.edit("**Nimbrung tololl, Nimbrung!!**")
    sleep(1)
    await typew.edit("**Sombong amat punya jempol,Gamau nimbrung**")
    sleep(1)
    await typew.edit("**Jempol lu kebas? Apa dah putus?**")
    sleep(2)
    await typew.edit("**NIMBRUNGGG GOBLOK!!!!**")


@register(outgoing=True, pattern='^.fck(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(".                       /¯ )\n"
                     "                      /¯  /\n"
                     "                    /    /\n"
                     "              /´¯/'   '/´¯¯`•¸\n"
                     "          /'/   /    /       /¨¯\\ \n"
                     "        ('(   (   (   (  ¯~/'  ')\n"
                     "         \\                        /\n"
                     "          \\                _.•´\n"
                     "            \\              (\n"
                     "              \\  ")

@register(outgoing=True, pattern='^.tp(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**INTINYA JANGAN LUPA MASUK!!**\n\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM\n"
                     "@TEMAN_RANDOM")
CMD_HELP.update({
    "vip":
    "`.bulan` ; `.hati` ; `.gbn` ; `.tolol` ; `.gmt`\
    \nUsage: liat aja.\
    \n\n`.heli` ; `.tank` ; `.tembak`\n`.bundir`\
    \nUsage: liat sendiri.\
    \n\n`.y` ; `.uasu`\
    \nUsage: jempol & Cek dyno\
    \n\n`.tawa` ; `.oy` ; `.fck` ; `.tp`\
    \nUsage: ketawa lari , Nyuruh nimbrung, fuck, Coba sendiri.\
    \n\n`.ular` ; `.babi` ; `.ajg`\
    \nUsage: liat sendiri."
})
