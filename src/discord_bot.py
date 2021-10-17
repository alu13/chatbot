import discord
from chatterbotter import get_response_gpt
import os
from dotenv import load_dotenv
load_dotenv()
client = discord.Client()
DISCORD_KEY = os.getenv('DISCORD_KEY')



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    yenach_call = '!Yenach_bot '
    if message.content.startswith(yenach_call):
        start_length = len(yenach_call)
        question = message.content[start_length:]
        print(question)
        response = get_bot_response(question)
        await message.channel.send(response)

def get_bot_response(question):
  response = get_response_gpt(question)
  return(response)

client.run(DISCORD_KEY)