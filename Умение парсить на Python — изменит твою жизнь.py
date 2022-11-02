# -- coding: utf-8 --
from bs4 import BeautifulSoup
import requests

x = 0

while True:
    if x == 0:
        url = "https://news.ycombinator.com/newest"
    else:
        url = "https://news.ycombinator.com/newest" + nexx

    request = requests.get(url)

    soup = BeautifulSoup(request.text, "html.parser")  # all info
    # print(soup)  #title
    teme = soup.find_all('td', class_='title')  # берем заголовки

    for temes in teme:
        temes = temes.find('a', {'class': 'storylink'})
        # print(temes)

        if temes is not None and 'github.com' in str(temes):
            print(temes.text)
            sublink = temes.get('href')
            print(str(temes.text) + " " + str(sublink))
            print("===")

    nex = soup.find(class_='morelink')
    nextlink = nex.get('href')      #проблемка

    nexx = nextlink[6:]
    x += 1





