import os

import requests
import time
import os
import random
import logging
import coloredlogs
import threading
import sys
import string


header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}

emails = ["@gmail.com", "@hotmail.com","@aim.com", "@yahoo.com", "@yandex.com", "@protonmail.com", "@live.com", "@zoho.com"]


logger = logging.getLogger(__name__)
fmt = ("[%(asctime)s] - %(message)s")
coloredlogs.install(fmt=fmt, logger=logger)

banner = ('''\033[0;91m
 /$$$$$$$   /$$$$$$           /$$$$$$                      /$$   /$$                        
| $$__  $$ /$$__  $$         |_  $$_/                     |__/  | $$                        
| $$  \\ $$|__/  \\ $$  /$$$$$$  | $$   /$$$$$$$  /$$    /$$ /$$ /$$$$$$    /$$$$$$   /$$$$$$$
| $$$$$$$/  /$$$$$$/ /$$__  $$ | $$  | $$__  $$|  $$  /$$/| $$|_  $$_/   /$$__  $$ /$$_____/
| $$____/  /$$____/ | $$  \\ $$ | $$  | $$  \\ $$ \\  $$/$$/ | $$  | $$    | $$$$$$$$|  $$$$$$ 
| $$      | $$      | $$  | $$ | $$  | $$  | $$  \\  $$$/  | $$  | $$ /$$| $$_____/ \\____  $$
| $$      | $$$$$$$$| $$$$$$$//$$$$$$| $$  | $$   \\  $/   | $$  |  $$$$/|  $$$$$$$ /$$$$$$$/
|__/      |________/| $$____/|______/|__/  |__/    \\_/    |__/   \\___/   \\_______/|_______/ 
                    | $$                                                                    
                    | $$                                                                    
                    |__/\033[00m\033[0;32m
                                     ----------------------               
                                   --[WRITTEN BY BACKSLASH]--
                                     ----------------------
              \033[00m\033[0;37m python points2prizesGen.py -t (amount of threads) -u (referral)

\033[00m''')               
print(banner)

def gen(email,password,proxy,link):
    #r = requests.get(link,proxies=proxy,headers=header)
    data = {"email:":email}
    r = requests.post(link, data,proxies=proxy,headers=header,)
    if 'class=\"account-points-total\">0</strong>' not in r.text:
        logger.info(f"Generated Account: {email}|{password} - [STATUS]:REDEEMED INVITE LINK")
        f.write(f"{email}|{password}\n")
    elif "IP Address Already Used"  in r.text:
        logger.warning("Proxy has already been used.")
    else:
        logger.error(f"Unable To Claim Rewards For: {email} - {proxy}")

def getProxy():
    list = open("proxies.txt", "r").readlines()
    while(True):
        try:
            proxy = {"http": "http://{}".format(random.choice(list).rstrip())}
            if(len(proxy['http']) <= 1):
                continue
            ret = requests.get("http://www.google.com", proxies=proxy, timeout=5)
            return proxy
        except Exception as error:
            pass
            #logger.error(f"ERROR - {error}")
'''
def getEmail():
    list = open("emails.txt","r+").readlines()
    try:
        username = ('{[0]}').format(random.choice(list).rsplit('|'))
    except Exception as e:
        logger.error(f"ERROR: {e}")
'''
def getEmail():
    email = ('').join(random.choices(string.ascii_letters + string.digits, k=8)) + random.choice(emails)
    return email

def getPass():
    password = ('').join(random.choices(string.ascii_letters + string.digits, k=8))
    return password
''' 
link = input("Ref Link: ")
threads = int(input("Number of Threads: "))
#https://www.pointsprizes.com/ref/18129999
for t in range(threads):
    threading.Thread(target=gen, args=(getUsername(),getProxy(),link)).start()

'''
#python points2prizesGen.py -t 5 -u "https://www.pointsprizes.com/ref/18129999"

if len(sys.argv) == 5:
    logger.info(f"[THREADS]: {sys.argv[2]} + [URL]: {sys.argv[4]}")
    threads = int(sys.argv[2])
    for t in range(threads):
        f = open("genned.txt", 'r+')
        threading.Thread(target=gen, args=(getEmail(),getPass(),getProxy(),sys.argv[4])).start()
else:
    print(len(sys.argv))
    print(banner)