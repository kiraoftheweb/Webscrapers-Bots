import logging
import coloredlogs
import requests
from bs4 import BeautifulSoup


LOGGER = logging.getLogger(__name__)
FMT = ("%(asctime)s - %(message)s")
coloredlogs.install(fmt=FMT, logger=LOGGER)
F = open("proxyListPl.txt", "w+")

HEADERS = requests.utils.default_headers()
HEADERS.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})


URL = "https://proxylist.pl"
PAGE = requests.get(URL, headers=HEADERS)
CONTENT = PAGE.text
SOUP = BeautifulSoup(CONTENT, 'lxml')
PROXIES = SOUP.find_all('span')

for P in PROXIES:
    LOGGER.info(P.text)
    F.write(P.text + "\n")
    
