import discord

client = discord.Client()

token = '[TOKEN HERE]'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!watch'):
        roomCode = message.content[7:]
        watchLink = f'https://vynchronize.herokuapp.com/{roomCode}' #link for synchronous video watching
        await message.channel.send(f'@{message.author} ' +  watchLink)

client.run(token)