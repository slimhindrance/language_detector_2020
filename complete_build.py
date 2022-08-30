from __future__ import unicode_literals
import pandas as pd
import bs4
import requests
import youtube_dl

base = "https://www.youtube.com/results?search_query="
data = pd.read_csv("languages.csv")
lang_column = data['Language ']
languages = []

for x, y in lang_column.iteritems():
    languages.append(y)


subtit = "+movies+with+english+subtitles"
searches = base.join(languages) + subtit

for langnum in range(0,100):
    r = requests.get(base+languages[langnum]+ subtit)
# searches is list of 100 searches for language+movies+with+english+subtitles


    page = r.text
    soup = bs4.BeautifulSoup(page, 'html.parser')

    vids = soup.findAll('a', attrs={'class': 'yt-uix-tile-link'})

    video_list = []
    for v in vids:
        tmp = 'https://www.youtube.com' + v['href']
        video_list.append(tmp)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
        'postprocessor_args': [
        '-ar', '16000'
    ],
        'prefer_ffmpeg': True,
        'keepvideo': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(video_list)
