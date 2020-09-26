import discord

client = discord.Client()

watchLink = '' #link for synchronous video watching


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!watch'):
        await message.channel.send(f'@{message.author}' +  watchLink)

client.run('[ENTER TOKEN HERE]')