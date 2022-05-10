import discord
import random 

    #Token received from setting up BOT/ Discord server 

TOKEN = 'OTU2Nzc0MjIxMzExMjc1MDUw.Yj1Hbg.FBmPXYzOSb8Xpg-6MKnPUqb62AA'

#must create a connection between discord and the bot from discord 
client = discord.Client()

#this is the bot start up function, when the bot is online the terminal 'we have logged in as in this eg RalphieBot#6825
@client.event 
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# in order to read and respond to the messages i've created another async function def on message and set variables 
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

      # so that the doesn't respond to itself creating an infinite loop

    if message.author == client.user:
        return


       # Connecting messages to the name which is this example the name of the bot
       # next is the user message, which is set to respond upper and lower 

    if message.channel.name == 'ralphiebot':
      if user_message.lower() == 'hello':
          await message.channel.send(f'Hello {username}!')
          return 
      elif user_message.lower() == 'bye':
          await message.channel.send(f'See you later {username}!')
          return 
      elif  user_message.lower() == '!random':
           response = f'This is your random number: {random.random.randrange(10000000)}'
           await message.channel.send(response)
           return 

#code to allow to send messages in any channel on discord 
    if  user_message.lower() == '!anywhere':
         await message.channel.send('This can be used anywhere!')
         return

  # code to run the token which is the connection to the bot   

client.run(TOKEN)