import discord
import logging
import coloredlogs
import re
import requests

logger = logging.getLogger(__name__)
fmt = ("[%(asctime)s] - %(message)s")
coloredlogs.install(fmt=fmt, logger=logger)

def settings():
    result = {}
    with open('settings.ini', 'r') as settings: 
        for line in settings:
            name, value = line.rstrip().split('= ', 2)
            result[name.strip().lower()] = value
    return result

values = settings()
if len(values) != 1:
    raise ValueError("Not given all results")

token = values['[token]']

r = requests

class Client(discord.Client):
    async def on_ready(self):
        try:
            logger.info('Bot {} ready'.format(self.user))
        except Exception as err:
            logger.error("Exception occured during join call: %s", err)

    async def on_message(self, message):
        try:
            if 'discord.gift' in message.content:
                code = re.search("discord.gift/(.*)", message.content).group(1)
                if len(code) in range(15,20):
                    result = r.post('https://discordapp.com/api/v6/entitlements/gift-codes/'+code+'/redeem', json={"channel_id":str(message.channel.id)}, headers={'authorization':token}).text
                    if 'This gift has been redeemed already.' in result:
                        logger.warning("Code has already been redeemed.")
                    elif 'Unknown Gift Code' in result:
                        logger.warning("Invalid Nitro Code")
                    elif 'nitro' in result:
                        logger.info("Nitro Code Claimed")
                else:          
                    logger.critical("Invalid Nitro Code")
        except:
            pass

def main():
    client = Client()
    client.run(token, bot=False)

if __name__ == "__main__":
    main()

