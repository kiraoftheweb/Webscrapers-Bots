import requests, sys, logging, coloredlogs
from sys import argv
from os import system
import json

log = logging.getLogger(__name__)
hax = ("[%(asctime)s] - %(message)s")
coloredlogs.install(fmt=hax, logger=log)

f = open("results.txt", "w+")

scraper = (requests.get("https://api.github.com/users/backslash/starred?page=1&per_page=100").text).split('"')

indices = [i for i, x in enumerate(scraper) if "clone_url" in x]

f = open("starred.txt", "w")
print(len(indices))
while r < (len(indices)):
    d = int(indices[r])
    print(scraper[d + 2])
    f.write(f"{scraper[d +2]}\n")
