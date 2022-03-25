import discord
import random 

TOKEN = 'OTU2Nzc0MjIxMzExMjc1MDUw.Yj1Hbg.FBmPXYzOSb8Xpg-6MKnPUqb62AA'

client = discord.Client()

@client.event 
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


client.run(TOKEN)