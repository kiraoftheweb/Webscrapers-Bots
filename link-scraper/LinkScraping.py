import logging
import coloredlogs
import requests
from bs4 import BeautifulSoup
import re

logger = logging.getLogger(__name__)
fmt = ("%(asctime)s - %(message)s")
coloredlogs.install(fmt=fmt, logger=logger)
f = open("ScrapedLinks.txt", "w+")

HEADERS = requests.utils.default_headers()
HEADERS.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})


URL = ""
PAGE = requests.get(URL, headers=HEADERS)
CONTENT = PAGE.text
soup = BeautifulSoup(CONTENT, 'lxml')
links = [a.get('href') for a in soup.find_all('a', href=True)]


for link in links:
    if "http://" in link:
        logger.info(link)
        f.write(link + "\n")
    elif "https://" in link:
        logger.info(link)
        f.write(link + "\n")
    else:
        pass