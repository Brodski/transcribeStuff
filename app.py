from __future__ import unicode_literals
from flask import Flask
# from aioflask import Flask
import asyncio

import requests 
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession

import youtube_dl
import yt_dlp

import time


app = Flask(__name__)

@app.route('/')
def home():
    # Links to all other routes in the app.
    return """
    <h1>Links to all other routes in the app.</h1>
    <ul>
        <li><a href="/yo">/yo</a></li>
        <li><a href="/test">/test scrapes ycombinator</a></li>
        <li><a href="/yt">/yt Gangnam style</a></li>
        <li><a href="/yt1">/yt1 extract_info </a></li>
        <li><a href="/gera">/gera gera stuff </a></li>
    </ul>

    """

@app.route('/yo/<text>')
@app.route('/yo/')
def yo(text="brother"):
    return "Yo {}".format(text)

@app.route('/gera/')
async def gera():
    channel = "lolgeranimo"
    url = f'https://www.twitch.tv/{channel}/videos?filter=archives&sort=time'
    session = AsyncHTMLSession()
    # await for the response
    
    res = await session.get(url)
    await res.html.arender()
    # Use the BeautifulSoup library to parse the webpage.
    # print(res)
    # print(res.status_code)
    # print(res.links)
    # print(res.content)
    # soup = BeautifulSoup(res.text, 'html.parser')
    # # Select all the elements with the class storylink
    
    # print(soup.prettify())
    # links = soup.select('a[href^="/videos/"]')
    # print(links)
    return "links"

@app.route('/test/')
def test():
    # scrape a webpage and print the results to the terminal. 
    # Use the requests library to download the webpage.
    res = requests.get('https://news.ycombinator.com/news')
    # Use the BeautifulSoup library to parse the webpage.
    print(res)
    soup = BeautifulSoup(res.text, 'html.parser')
    # Select all the elements with the class storylink
    
    print(soup)
    links = soup.select('.titleline')
    print(links)

    # Select all the elements with the class score
    subtext = soup.select('.subtext')
    # Create a custom function to create a custom dictionary from the HN elements.
    def create_custom_hn(links, subtext):
        hn = []
        for idx, item in enumerate(links):
            title = links[idx].getText()
            href = links[idx].get('href', None)
            vote = subtext[idx].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points > 99:
                    hn.append({'title': title, 'link': href, 'votes': points})
        return hn
    def print_results(hnlist):
        for idx, item in enumerate(hnlist):
            print('{}. {} - {} points'.format(idx, item['title'], item['votes']))
    # Call the custom function to create a custom dictionary from the HN elements.
    hn = create_custom_hn(links, subtext)
    # Call the custom function to print the results to the terminal.
    print_results(hn)

    return "Test"


@app.route('/yt/')
def yt():
    def my_hook(d):
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')
        if d['status'] == 'filename':
            print('Filename=====', d['filename'])
        if d['status'] == 'downloaded_bytes':
            print('downloaded_bytes=====', d['downloaded_bytes'])
        if d['status'] == 'total_bytes':
            print('total_bytes=====', d['total_bytes'])
        if d['status'] == 'total_bytes_estimate':
            print('total_bytes_estimate=====', d['total_bytes_estimate'])
        if d['status'] == 'elapsed':
            print('elapsed=====', d['elapsed'])
        if d['status'] == 'eta':
            print('eta=====', d['eta'])
        if d['status'] == 'speed':
            print('speed=====', d['speed'])
        if d['status'] == 'fragment_index':
            print('fragment_index=====', d['fragment_index'])


    ydl_opts = {
        # 'format': 'bestaudio/best',
        # 'format': 'worstvideo+bestaudio',
        # 'format': '(worstvideo+bestaudio)',
        'format': 'worst',
        "verbose": True,
        # "listformats": True,
        # 'postprocessors': [{
        #     'key': 'FFmpegExtractAudio',
        #     'preferredcodec': 'mp3',
        #     'preferredquality': '0', #https://trac.ffmpeg.org/wiki/Encode/MP3
            # 'preferredquality': '192', #https://trac.ffmpeg.org/wiki/Encode/MP3
                                        #https://github.com/ytdl-org/youtube-dl/blob/195f22f679330549882a8234e7234942893a4902/youtube_dl/postprocessor/ffmpeg.py#L302
        # }],
        # 'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.twitch.tv/videos/1637006503'])
        # ydl.download(['https://www.youtube.com/watch?v=9bZkp7q19f0'])
    # measure execution time of a code snippet. start time and end time difference is the execution time.
    start_time = time.time()
    
    print("GOGOGOOG--- ", start_time)
    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #      ydl.download(['https://www.youtube.com/watch?v=9bZkp7q19f0'])
         
    end_time = time.time() 
    print("GOGOGOOG ---- ", end_time)
    print("BAM ---- ", end_time - start_time )
    print("BAM ---- ", end_time - start_time )
    print("BAM ---- ", end_time - start_time )
    print("BAM ---- ", end_time - start_time )
    print("BAM ---- ", end_time - start_time )
    print("BAM ---- ", end_time - start_time )
    return "YT"

@app.route('/yt1/')
def yt1():
    ydl_opts = {}

    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    with ydl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(
            'https://www.youtube.com/watch?v=9bZkp7q19f0', download=True) 

    # print('meta : %s' %(meta))
    print('--------------------')
    print('upload date : %s' %(meta['upload_date']))
    print( 'uploader    : %s' %(meta['uploader']))
    print( 'views       : %d' %(meta['view_count']))
    print( 'likes       : %s' %(meta.get('like_count', 'nope')))
    print( 'dislikes    : %s' %(meta.get('dislike_count', 'no dislikes')))
    print( 'id          : %s' %(meta['id']))
    print( 'format      : %s' %(meta['format']))
    print( 'duration    : %s' %(meta['duration']))
    print( 'title       : %s' %(meta['title']))
    print('description : %s' %(meta['description']))
    return 'bam'
if __name__ == "__main__":
    app.run(debug=True)

