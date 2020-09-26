import discord, asyncio, os, requests

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
        watchLink = f'https://cmu-spectre.herokuapp.com/api/{vidID}'
        botmessage = await message.channel.send('Happy watching! ' +  watchLink)
        await botmessage.edit(suppress=True)

    if not message.content.startswith('!watch'):
        otherMessages = message.content
        r = requests.post('https://cmu-spectre.herokuapp.com/', otherMessages)
        print(r.url, message.content)

client.run(os.environ['BOT_TOKEN'])