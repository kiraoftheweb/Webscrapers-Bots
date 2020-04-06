import requests
import threading
import time
import sys
import os
import threading
import websocket
from bs4 import BeautifulSoup 
import random
import logging
import coloredlogs
import re

logger = logging.getLogger(__name__)
fmt = ("%(asctime)s - %(message)s")
coloredlogs.install(fmt=fmt, logger=logger)


headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}

def dislike(link,proxy):
	s = requests.Session()
	'''
	soup = BeautifulSoup(s.post(link).content, 'lxml')
	'''

	try:
		data = {
		"viewkey": link.split("=")[1]
		}
		page = s.post(link,headers=headers,proxies=proxy,data=data,timeout=5)

		soup = BeautifulSoup(s.post(link).content, 'lxml')
		token = soup.find("input",attrs={"name":"token"})["value"]
		#logger.info("USERTOKEN: "+ token)
		videoID = soup.find("input",attrs={"name":"attachment"})["value"]
		#logger.info("VIDEO-ID: "+ videoID)

		dislikes = soup.find("span", {"class": "votesDown"})
		likes = soup.find("span", {"class": "votesUp"})
		#totalLikes = ((likes.split("<"))[1]).split(">")[1]
		#totalDislikes = ((dislikes.split("<"))[1]).split(">")[1]

		#logger.info("DISLIKES: " + str(dislikes))
		#logger.info("LIKES: " + str(likes))
		data = {
		"id" : videoID,
		"token" : token,
		"current" : "1",
		"value" : "0", #Upvote or downvote
		}
		url = f"https://www.pornhub.com/video/rate?id={videoID}&token={token}&current=1&value=0"
		final = s.post(url, headers=headers,cookies=s.cookies,data=data,proxies=proxy,timeout=5)
		if final.status_code == 200:
			s.post("https://www.pornhub.com/view_video.php?viewkey=ph5e68b0de88a45","https://www.pornhub.com/view_video.php?viewkey=ph5e68b0de88a45")
			logger.info(f"Disliked Video")
		else:
			logger.critical("Error")

	except:
		logger.critical("Proxy Error")
		pass


def view(link,proxy):
	s = requests.Session()

	try:
		data = {
		"viewkey": link.split("=")[1]
		}
		page = s.get(link,headers=headers,proxies=proxy,cookies=s.cookies,timeout=5)
		if page.status_code == 200:
			logger.info("Viewed Video")
		else:
			logger.critical("Proxy Error")
			pass

	except:
		logger.critical("Proxy Error")
		pass


def like(link,proxy):
	s = requests.Session()
	'''
	soup = BeautifulSoup(s.post(link).content, 'lxml')
	'''

	try:
		page = s.post(link,headers=headers,proxies=proxy,timeout=5)

		soup = BeautifulSoup(s.post(link).content, 'lxml')
		token = soup.find("input",attrs={"name":"token"})["value"]
		#logger.info("USERTOKEN: "+ token)
		videoID = soup.find("input",attrs={"name":"attachment"})["value"]
		#logger.info("VIDEO-ID: "+ videoID)

		dislikes = soup.find("span", {"class": "votesDown"})
		likes = soup.find("span", {"class": "votesUp"})
		#totalLikes = ((likes.split("<"))[1]).split(">")[1]
		#totalDislikes = ((dislikes.split("<"))[1]).split(">")[1]

		#logger.info("DISLIKES: " + str(dislikes))
		#logger.info("LIKES: " + str(likes))
		data = {
		"id" : videoID,
		"token" : token,
		"current" : "1",
		"value" : "1", #Upvote or downvote
		}
		url = f"https://www.pornhub.com/video/rate?id={videoID}&token={token}&current=1&value=1"
		final = s.post(url, headers=headers,cookies=s.cookies,data=data,proxies=proxy,timeout=5)
		if final.status_code == 200:
			s.post("https://www.pornhub.com/view_video.php?viewkey=ph5e68b0de88a45","https://www.pornhub.com/view_video.php?viewkey=ph5e68b0de88a45")
			logger.info(f"Liked Video")
		else:
			logger.critical("Error")

	except:
		logger.critical("Proxy Error")
		pass



def getproxy():
	list = open("proxies.txt", "r").readlines()
	while(True):
		try:
			proxy = {"https": "https://{}".format(random.choice(list).rstrip())}
			if(len(proxy['https']) <= 1):
				continue
			ret = requests.get("https://www.google.com", proxies=proxy, timeout=5)
			return proxy
		except:
			pass


banner = print("""
\033[0;96m╔════════════════════════════════════════════╗\033[00m  
\033[0;96m║            \033[0;91m╔╗ ╔╗  ╔╗ ╔══╗   ╔╗\033[00m             \033[0;96m║\033[00m\033[00m  
\033[0;96m║            \033[0;91m║║ ║║  ║║ ║╔╗║  ╔╝╚╗\033[00m            \033[0;96m║\033[00m\033[00m  
\033[0;96m║            \033[0;91m║╚═╝╠╗╔╣╚═╣╚╝╚╦═╩╗╔╝\033[00m            \033[0;96m║\033[00m\033[00m  
\033[0;96m║            \033[0;91m║╔═╗║║║║╔╗║╔═╗║╔╗║║\033[00m             \033[0;96m║\033[00m\033[00m  
\033[0;96m║            \033[0;91m║║ ║║╚╝║╚╝║╚═╝║╚╝║╚╗\033[00m            \033[0;96m║\033[00m\033[00m  
\033[0;96m║            \033[0;91m╚╝ ╚╩══╩══╩═══╩══╩═╝\033[00m            \033[0;96m║\033[00m\033[00m  
\033[0;96m╚════════════════════════════════════════════╝\033[00m  \033[0;1m
	   \033[0;96m    ╔═════════════╗
	       ║\033[0;91mBy: Backslash\033[0;96m║\033[00m
	       \033[0;96m╚═════════════╝\033[00m\033[0;90m
\033[0;96m╔═════════════════════════╦══════════════════╗\033[00m
\033[0;96m║\033[0;91m      like (videolink)\033[0;96m   ║\033[0;91m Bots Likes       \033[00m\033[0;96m║\033[00m\033[00m
\033[0;96m║\033[0;91m      dislike (videolink)\033[0;96m║\033[0;91m Bots Dislikes    \033[00m\033[0;96m║\033[00m\033[00m
\033[0;96m║\033[0;91m      view (videolink)\033[0;96m   ║\033[0;91m Bots Views       \033[00m\033[0;96m║\033[00m\033[00m
\033[0;96m║\033[0;91m      help\033[0;96m               ║\033[0;91m Shows this menu  \033[00m\033[0;96m║\033[00m\033[00m
\033[0;96m╚═════════════════════════╩══════════════════╝\033[00m
\033[00m""")

if len(sys.argv) < 3:
	banner

elif sys.argv[1] == "like":
	logger.info(f"Starting Like Bot On: {sys.argv[2]}")
	for i in range(250):
		proxy = getproxy()
		threading.Thread(target=like,args=(sys.argv[2], proxy)).start()

elif sys.argv[1] == "dislike":
	logger.info(f"Starting Dislike Bot On: {sys.argv[2]}")
	for i in range(100):
		proxy = getproxy()
		threading.Thread(target=dislike,args=(sys.argv[2], proxy)).start()

elif sys.argv[1] == "view":
	for i in range(10000):
		proxy = getproxy()
		threading.Thread(target=view,args=(sys.argv[2], proxy)).start()
else:
	pass






'''
DATA
'''

#https://www.pornhub.com/video/rate?id=291948392&token=MTU4Mzk3OTI5MXKmp-yIISeCqLkQHLTfX6--10oeDUkABmnwzdmuQI_o4Z8qKiNYEflcT3PlIyja82tJ43eTO-naAtxUMzjYPhI.&current=1&value=0
#                                   ^ID           ^Token                                                                                                       ^current     ^If its a thumbs down its zero if its a thumbs up then its a one

'''
# General
	Request URL: https://www.pornhub.com/video/rate?id=291948392&token=MTU4Mzk3OTI5MXKmp-yIISeCqLkQHLTfX6--10oeDUkABmnwzdmuQI_o4Z8qKiNYEflcT3PlIyja82tJ43eTO-naAtxUMzjYPhI.&current=1&value=0
	Request Method: POST
	Status Code: 200 OK
	Remote Address: 66.254.114.41:443
	Referrer Policy: no-referrer-when-downgrade
# Response Headers
	Content-Type: application/json; charset=utf-8
	Date: Thu, 12 Mar 2020 02:14:59 GMT
	Rating: RTA-5042-1996-1400-1577-RTA
	Server: openresty
	Transfer-Encoding: chunked
	Vary: User-Agent
	X-Frame-Options: SAMEORIGIN
# Request Headers
	Accept: */*
	Accept-Encoding: gzip, deflate, br
	Accept-Language: en-US,en;q=0.9
	Connection: keep-alive
	Content-Length: 0
	Cookie: ua=97fc230848bc304ccee289a55f3e5339; platform_cookie_reset=pc; platform=pc; bs=w7v4glswxuoov9d96pit1x2xqsn8iw97; ss=961280643457274033; RNLBSERVERID=ded6646
	DNT: 1
	Host: www.pornhub.com
	Origin: https://www.pornhub.com
	Referer: https://www.pornhub.com/view_video.php?viewkey=ph5e68b0de88a45
	Sec-Fetch-Dest: empty
	Sec-Fetch-Mode: cors
	Sec-Fetch-Site: same-origin
	User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36
	X-Requested-With: XMLHttpRequest
# Query String Parameters
	id: 291948392
	token: MTU4Mzk3OTI5MXKmp-yIISeCqLkQHLTfX6--10oeDUkABmnwzdmuQI_o4Z8qKiNYEflcT3PlIyja82tJ43eTO-naAtxUMzjYPhI.
	current: 1
	value: 0
'''
#	cookie = page.cookies['bs']
#print(cookie)