from discord import app_commands
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os
import datetime
import pytz

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')
ANNOUNCEMENT_CHANNEL_ID = int(os.getenv('ANNOUNCEMENT_CHANNEL_ID'))
NOTIFY_DAY = int(os.getenv('NOTIFY_DAY'))
NOTIFY_HOUR = int(os.getenv('NOTIFY_HOUR'))
NOTIFY_MINUTE = int(os.getenv('NOTIFY_MINUTE'))
PING_ROLE_ID = os.getenv('PING_ROLE_ID')

class Notify(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.notify.start()
        print(f'Cog: Started Notify')

    def cog_unload(self):
        self.notify.cancel()

    @tasks.loop(seconds=61)
    async def notify(self):
        current_Time = datetime.datetime.now(pytz.timezone('Europe/Amsterdam'))
        channel = self.client.get_channel(ANNOUNCEMENT_CHANNEL_ID)
        notify_Day = current_Time.weekday()  
        if notify_Day == NOTIFY_DAY:
            notify_Time = current_Time.strftime('%H:%M')

            next_saturday = current_Time + datetime.timedelta(days=5)
            next_saturday = next_saturday.replace(hour=11, minute=30, tzinfo=pytz.timezone('Europe/Amsterdam'))
            formatted_next_saturday = next_saturday.strftime("%d-%m-%Y at %H:%M")
            
            next_sunday = current_Time + datetime.timedelta(days=6)
            next_sunday = next_sunday.replace(hour=11, minute=30, tzinfo=pytz.timezone('Europe/Amsterdam'))
            formatted_next_sunday = next_sunday.strftime("%d-%m-%Y at %H:%M")
            
            if notify_Time == f'{NOTIFY_HOUR:02d}:{NOTIFY_MINUTE:02d}':
                invitation = await channel.send(f'**Attention <@&{PING_ROLE_ID}>!**\n The administratum has requested each of you to react with your possible attendance.\n :one: Saturday {formatted_next_saturday} \n :two: Sunday {formatted_next_sunday} \n :x: if you are a heretic.')
                await invitation.add_reaction('1️⃣')
                await invitation.add_reaction('2️⃣')
                await invitation.add_reaction('❌')
                