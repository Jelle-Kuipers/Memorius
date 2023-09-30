# imports
import discord
import os
import logging
from dotenv import load_dotenv

# retrieve ENV values
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

#setup bot logging
handler = logging.FileHandler(filename='memorius.log', encoding='utf-8', mode='w')

# declare scope for bot
intents = discord.Intents.default()
intents.message_content = True

# creates new client
client = discord.Client(intents=intents)

#once bot logs in, write in logs
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# reply to set message
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# run the bot         
client.run(BOT_TOKEN, log_handler=handler, log_level=logging.DEBUG)