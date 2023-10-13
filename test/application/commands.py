# commands.py
import os
from dotenv import load_dotenv 
import discord

# load used environment variables
load_dotenv()
GUILD_ID = os.getenv('GUILD_ID')

async def setup_application_commands(bot, client):
    @bot.command(name="pong", description="current ping in MS of the bot", guild=discord.Object(id=GUILD_ID))
    async def ping(interaction):
        delay = round(client.latency * 1000)
        await interaction.response.send_message(f"```Servo Skull #8969, Designation [Ludicarum Bellorum Memorius]```Is currently experiencing a delay of **{delay}ms**.")

    @bot.command(name="hello", description = "application command test", guild=discord.Object(id=GUILD_ID))
    async def first_command(interaction):
        await interaction.response.send_message("Welcome, master")
   
    await bot.sync(guild=discord.Object(id=GUILD_ID))
    if GUILD_ID == 963747264990437386: #TODO: Remove debug code, only meant to know what server I am deploying to :)
        guild = 'Warhammer Server'
    else:
        guild = 'Testing Environment'
    print(f'Module: Application_Commands, has been awoken in [{guild}].')