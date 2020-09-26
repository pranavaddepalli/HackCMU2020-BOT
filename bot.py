import discord, requests, asyncio, os
from dotenv import load_dotenv

client = discord.Client()
load_dotenv('.env')

#token = 'NzU5MTkyMzcwOTUxNzQ5NjUy.X256_g.2bdu08Gm4x79cex3P2b-rQx8Xrg'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!watch'):
        await message.edit(suppress=True)
        vidURL = message.content[7:]
        vidID = vidURL[vidURL.index('=')+1:]
        watchLink = f'https://youtube-party-bot.herokuapp.com/api/{vidID}'
        await message.channel.send('Happy watching! ' +  watchLink)

client.run(os.getenv('BOT_TOKEN'))