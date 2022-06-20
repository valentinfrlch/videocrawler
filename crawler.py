# take a url as argument

import kwargs
import requests
from bs4 import BeautifulSoup


def crawler(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # find all the links in the page
    links = soup.find_all('a')
    output = []
    for link in links:
        try:
            # crawl the link
            # get the html
            r = requests.get(link.get('href'))
            # parse with BeautifulSoup
            soup = BeautifulSoup(r.text, 'html.parser')
            # find all video links
            videos = soup.find_all('video')
            # add the video links to the output
            for video in videos:
                print(url + video.get('src'))
                output.append(url + video.get('src'))

        except Exception as e:
            continue
    return output


print(crawler('https://www.ardmediathek.de'))
