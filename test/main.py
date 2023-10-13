import discord
from discord import app_commands
from application.commands import setup_application_commands
from application.events import setup_application_events
import logging
import os
from dotenv import load_dotenv

#load ENV
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')

#logging
handler = logging.FileHandler(filename='memorius.log', encoding='utf-8', mode='w')

#defining client intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = app_commands.CommandTree(client)

#Once online, run
@client.event
async def on_ready():
    print(f'Awakening machine spirit of: {client.user}')
    setup_application_events(client) #Enables event based actions
    await setup_application_commands(bot, client) #Sets up commands to be synced
    print(f'Machine spirit awakened, praise the Omnissiah!')
client.run(BOT_TOKEN, log_handler=handler)