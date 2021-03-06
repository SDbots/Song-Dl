

import os
import requests
import aiohttp
import youtube_dl
from pytube import YouTube
from SongBot import Jebot as app
from pyrogram import filters, Client
from youtube_search import YoutubeSearch
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputTextMessageContent

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

@app.on_message(filters.command('song'))
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('๐๐ง๐ค๐๐๐จ๐จ๐๐ฃ๐ โขโขโข ๐')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)

        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]
        yt = YouTube(link)
    except Exception as e:
        m.edit(
            "โ Found Nothing.\n\nTry another keywork or maybe spell it properly."
        )
        print(str(e))
        return
    m.edit("๐ฟ๐ค๐ฌ๐ฃ๐ก๐ค๐น๐๐ฃ๐ ๐จ๐ค๐ฃ๐โขโขโข๐")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = '๐ต ๐๐ฅ๐ก๐ค๐๐๐๐ ๐๐ฎ @TheAnkiVectorbotโขโขโข\n ๐๐ค๐๐ฃ @slhitbotofficial โขโขโข'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        s = message.reply_audio(audio_file, caption=rep, thumb=thumb_name, parse_mode='md', title=title, duration=dur, performer=str(yt.author))
        m.delete()
    except Exception as e:
        m.edit('โ Error\n Report @slhitbotofficial')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
