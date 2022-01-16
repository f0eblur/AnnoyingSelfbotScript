import sys

import discord

token = "Your Token Here"
trollUserId = TheirIdAsANumber

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author.id == trollUserId:
        async for message in message.channel.history(limit=1):
            TrollMessage = ""
            for at in message.attachments:
                TrollMessage += at.url + '\n'
            TrollMessage += message.content
            TrollMessage = TrollMessage.lower()

            New = ""
            a = False
            for i in range(len(TrollMessage)):
                if a == False:
                    a = True
                    New += TrollMessage[i].upper()
                else:
                    a = False
                    New += TrollMessage[i].lower()
            print(New)
            await message.channel.send(New)

client.run(token, bot=False)
