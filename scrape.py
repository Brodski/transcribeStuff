from __future__ import unicode_literals
from flask import Flask
# from aioflask import Flask

import requests 
from bs4 import BeautifulSoup
# from requests_html import AsyncHTMLSession
from requests_html import HTMLSession
from requests_html import AsyncHTMLSession

import youtube_dl
import yt_dlp

import time
import asyncio

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# use selenium to render the page and then scrape it with beautiful soup. 
# https://stackoverflow.com/questions/6028000/how-to-read-a-static-web-page-into-python

# https://stackoverflow.com/questions/6028000/how-to-read-a-static-web-page-into-python
import sys
import re


options = Options()
# options.add_argument('--headless')
browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)


async def gera():
    # scrape a webpage and print the results to the terminal.
    # Use the requests library to download the webpage.
    # res = requests.get('https://news.ycombinator.com/news')
    # make an asynchronous request to the webpage.

    channel = "lolgeranimo"
    url = f'https://www.twitch.tv/{channel}/videos?filter=archives&sort=time'
    # session = HTMLSession()
    # res = session.get(url)    
    # res.html.render(sleep=2)
    browser.get(url)
    # using selenium scroll to the bottom of the page to load all the videos.

    # print (browser.page_source)
    print (browser.title)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    
    browser.execute_script("""document.querySelector("[id='root'] main .simplebar-scroll-content").scroll(0, 10000)""")
    time.sleep(3)
    browser.execute_script("""document.querySelector("[id='root'] main .simplebar-scroll-content").scroll(0, 10000)""")
    time.sleep(3)
    
    
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    browser.quit()
    vids = soup.select("a[href^='/videos/']")
    print ("vids")
    print (vids)
    # for i in range(len(vids)):
        # print(i)
        # print(vids[i])
    allHrefs = []
    for tag in vids:
        allHrefs.append(tag['href'])
    allHrefs.sort()
    # for href in allHrefs:
    #     print(href)
    hrefsSet = set()
    for href in allHrefs:
        match = re.search(r'(/videos/\d+)(\?.*)', href)
        if match:
            print (match.group(1))
            hrefsSet.add(match.group(1))

    print ("hrefsSet")
    print ("hrefsSet")
    print ("hrefsSet")
    print ("hrefsSet")
    print ("hrefsSet")
    print ("hrefsSet")
    print ("hrefsSet")
    [print (hrefsSet) for hrefsSet in enumerate(hrefsSet)]
# [print('\n', vid.'href')) for vid  in enumerate(vids)]

    return "links"


    
if __name__ == "__main__":
    # run the gera() function
    # gera()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(gera())
    loop.close()

