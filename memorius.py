# imports
import discord
from discord.ext import tasks, commands
from discord import app_commands
import datetime
import os
import logging
from dotenv import load_dotenv

# retrieve ENV values
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')
ANNOUNCEMENT_CHANNEL_ID = int(os.getenv('ANNOUNCEMENT_CHANNEL_ID'))
NOTIFY_DAY = int(os.getenv('NOTIFY_DAY'))
NOTIFY_HOUR = int(os.getenv('NOTIFY_HOUR'))
PING_ROLE_ID = os.getenv('PING_ROLE_ID')

#setup bot logging
handler = logging.FileHandler(filename='memorius.log', encoding='utf-8', mode='w')

# define client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = app_commands.CommandTree(client)

current_Time = datetime.datetime.now()

# once online, print.
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    Notify(client)
    await bot.sync(guild=discord.Object(id=GUILD_ID))
    print(f'Command tree has been synced!')

# starts on bot launch    
class Notify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.notify.start()
        print(f'Started Notify')

    def cog_unload(self):
        self.notify.cancel()

    @tasks.loop(seconds=30)
    async def notify(self):
        channel = client.get_channel(ANNOUNCEMENT_CHANNEL_ID)
        notify_Day = current_Time.weekday()  
        if notify_Day == NOTIFY_DAY:
            notify_Time = current_Time.hour

            next_saturday = current_Time + datetime.timedelta(days=5)
            next_saturday = next_saturday.replace(hour=11, minute=30)
            formatted_next_saturday = next_saturday.strftime("%d-%m-%Y at %H:%M")
            
            next_sunday = current_Time + datetime.timedelta(days=6)
            next_sunday = next_sunday.replace(hour=11, minute=30)
            formatted_next_sunday = next_sunday.strftime("%d-%m-%Y at %H:%M")
            
            if notify_Time == NOTIFY_HOUR:
                invitation = await channel.send(f'**Attention <@&{PING_ROLE_ID}>!**\n The administratum has requested each of you to react with your possible attendance.\n :one: Saturday {formatted_next_saturday} \n :two: Sunday {formatted_next_sunday} \n :x: if you are a heretic.')
                await invitation.add_reaction('1️⃣')
                await invitation.add_reaction('2️⃣')
                await invitation.add_reaction('❌')
                
# scaffolding for any application command.
@bot.command(name="hello", description = "application command test", guild=discord.Object(id=GUILD_ID))
async def first_command(interaction):
    await interaction.response.send_message("Greetings master.")
    
# see ping of bot
@bot.command(name="ping", description = "current ping in MS of the bot", guild=discord.Object(id=GUILD_ID))
async def ping(interaction):
    delay = round(client.latency * 1000)
    await interaction.response.send_message(f"I am currently **{delay} ms** behind.")
 
client.run(BOT_TOKEN, log_handler=handler, log_level=logging.DEBUG)