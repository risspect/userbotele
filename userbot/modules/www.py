# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register
import time


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^Sping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**ð ADA BABIð **")
    await pong.edit("**ðð ADA BABI ðð**")
    await pong.edit("**ððð ADA BABI ððð**")
    await pong.edit("**ðððð LU BABI ðððð**")
    await pong.edit("**ððððð OINKK ððððð**")
    await pong.edit("**ðððððð OINKK ðððððð**")
    await pong.edit("**ððððððð OINKK ððððððð**")
    await pong.edit("`.................ð`")
    await pong.edit("`................ð.`")
    await pong.edit("`...............ð..`")
    await pong.edit("`..............ð...`")
    await pong.edit("`.............ð....`")
    await pong.edit("`............ð.....`")
    await pong.edit("`...........ð......`")
    await pong.edit("`..........ð.......`")
    await pong.edit("`.........ð........`")
    await pong.edit("`........ð.........`")
    await pong.edit("`.......ð..........`")
    await pong.edit("`......ð...........`")
    await pong.edit("`.....ð............`")
    await pong.edit("`....ð.............`")
    await pong.edit("`...ð..............`")
    await pong.edit("`..ð...............`")
    await pong.edit("`.ð................`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**ðNGOK!!** "
                    f"\n `%sms` \n"
                    f"**PEMILIK** "
                    f"\n  â¥ `{ALIVE_NAME}` \n" % (duration))

@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`Pong!`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit("`Pong!\n%sms`" % (duration))



@register(outgoing=True, pattern="^Lping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`ADA MONYET..............ðððð`")
    await pong.edit("`HUHU HAHA................ðððð`")
    await pong.edit("`HUHU HAHA................ððððð`")
    await pong.edit("`BERUBAH JADI SUNGGOKONG RAJA MONYETðð`")
    await pong.edit("**AKU ADALAH RAJA MONYET,KALIAN SEMUA ADALAH MONYET**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**ð!**\n"
                    f"ð **NYET:** "
                    f"`%sms` \n"
                    f"ð **Waktu:** "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^Xping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**S**")
    await pong.edit("**ST**")
    await pong.edit("**STR**")
    await pong.edit("**STRE**")
    await pong.edit("**STRES**")
    await pong.edit("**STRESS**")
    await pong.edit("**STRESS U**")
    await pong.edit("**STRESS US**")
    await pong.edit("**STRESS USE**")
    await pong.edit("**STRESS USER**")
    await pong.edit("**STRESS USERB**")
    await pong.edit("**STRESS USERBO**")
    await pong.edit("**STRESS USERBOT**")
    await pong.edit("STRESS!")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**ð PONG!**\n"
                    f"âªï¸ __Gawaras:__ "
                    f"`%sms` \n"
                    f"âªï¸ __STRESS:__ "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^Ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**PÌÌ¤IÌÌ¤NÌÌ¤GÌÌ¤**")
    await pong.edit("**pÌÌ²oÌÌ²nÌÌ²gÌÌ²**")
    await pong.edit("**á¦á¿ááá¦á¦**")
    await pong.edit("**Uà¾Sà¾Eà¾Rà¾Bà¾Oà¾Tà¾**")
    await pong.edit("**PÍ¦Ì¥IÍ¦Ì¥NÍ¦Ì¥GÍ¦Ì¥**")
    await pong.edit("**PÍ¦Ì¥OÍ¦Ì¥NÍ¦Ì¥GÍ¦Ì¥**")
    await pong.edit("**PÌIÌNÌGÌ**")
    await pong.edit("**PÌOÌNÌGÌ**")
    await pong.edit("**SÍÍTÍÍRÍÍEÍÍSÍÍSÍÍ UÍÍSÍÍEÍÍRÍÍBÍÍOÍÍTÍÍ**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**â¿´âÛªÛªâáâê¤ââââââ¼âÛªÛªâââÛªÛªÌ¸â¾ââââââ©âââà£¾ÝÝâ£** \n"
                    f"**                 âªPONG!âª** \n"
                    f"**â¿´âÛªÛªâáâê¤ââââââ¼âÛªÛªâââÛªÛªÌ¸â¾ââââââ©âââà£¾ÝÝâ£** \n"          
                    f"**â Sinyal  :** `%sms` \n"
                    f"**â Tuanku   :** `{ALIVE_NAME}` \n"
                    f"**â¼ââââââââââââââââââ¾** \n" % (duration)) 
          
    

@register (outgoing=True, pattern="^Speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("**......................................ðï¸**")
    await spd.edit("**.....................................ðï¸.**")
    await spd.edit("**....................................ðï¸..**")
    await spd.edit("**...................................ðï¸...**")
    await spd.edit("**..................................ðï¸....**")
    await spd.edit("**.................................ðï¸.....**")
    await spd.edit("**................................ðï¸......**")
    await spd.edit("**...............................ðï¸.......**")
    await spd.edit("**..............................ðï¸........**")
    await spd.edit("**.............................ðï¸.........**")
    await spd.edit("**............................ðï¸..........**")
    await spd.edit("**...........................ðï¸...........**")
    await spd.edit("**..........................ðï¸............**")
    await spd.edit("**.........................ðï¸.............**")
    await spd.edit("**........................ðï¸..............**")
    await spd.edit("**.......................ðï¸...............**")
    await spd.edit("**......................ðï¸................**")
    await spd.edit("**..........ð¨âð¦¯.TIIIIN..ðï¸.................**")
    await spd.edit("**.........ð¨âð¦¯MINGGIR..ðï¸..................**")
    await spd.edit("**.........ð¨âð¦¯GOBLOK..ðï¸...................**")
    await spd.edit("**.......ð¨âð¦¯REM NYA..ðï¸....................**")
    await spd.edit("**......ð¨âð¦¯.BLOOONG.ðï¸.....................**")
    await spd.edit("**......ð¨âð¦¯.YAUDHLHðï¸......................**")
    await spd.edit("**....ð¨âð¦¯Dasar....ðï¸.......................**")
    await spd.edit("**...ð¨âð¦¯ðï¸.................................**")
    await spd.edit("**.ðï¸ Orang Buta**")
    await spd.edit("ðï¸")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Hasil Tes:\n**"
                   "âº **Dimulai Pada:** "
                   f"`{result['timestamp']}` \n"
                   f" **âââââââââââââââââ**\n\n"
                   "âº **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "âº **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "âº **Ping:** "
                   f"`{result['ping']}` \n"
                   "âº **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "âº **BOT:** `STRESS Userbot`")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^Pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("**P**")
    await pong.edit("**PI**")
    await pong.edit("**PIN**")
    await pong.edit("**PING**")
    await pong.edit("**PING P**")
    await pong.edit("**PING PO**")
    await pong.edit("**PING PON**")
    await pong.edit("**PING PONG**")
    await pong.edit("`....................ðï¸`")
    await pong.edit("`...................ðï¸.`")
    await pong.edit("`..................ðï¸..`")
    await pong.edit("`.................ðï¸...`")
    await pong.edit("`................ðï¸....`")
    await pong.edit("`...............ðï¸.....`")
    await pong.edit("`..............ðï¸......`")
    await pong.edit("`.............ðï¸.......`")
    await pong.edit("`...........ðï¸.........`")
    await pong.edit("`..........ðï¸..........`")
    await pong.edit("`.........ðï¸...........`")
    await pong.edit("`........ðï¸............`")
    await pong.edit("`.......ðï¸.............`")
    await pong.edit("`......ðï¸..............`")
    await pong.edit("`....ðï¸................`")
    await pong.edit("`...ðï¸.................`")
    await pong.edit("`..ðï¸..................`")
    await pong.edit("`.ðï¸...................`")
    await pong.edit("`DUARRRR KONTOLL.....ð¥ð¤¯ð£`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit("ð¡ **STRESS!**\n`%sms`" % (duration))

CMD_HELP.update(
    {"ping": "`Ping` ; `Lping` ; `Xping` ; `Sping`\
    \nUsage: Untuk menunjukkan ping bot.\
    \n\n`Speed`\
    \nUsage: Untuk menunjukkan kecepatan.\
    \n\n`Pong`\
    \nUsage: sama kaya perintah ping."
     })
