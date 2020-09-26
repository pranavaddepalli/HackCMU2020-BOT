import discord, asyncio, os

client = discord.Client()

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

client.run(os.environ['BOT_TOKEN'])