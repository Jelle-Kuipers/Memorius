# imports
import discord
from discord.ext import tasks, commands
from discord import app_commands
import datetime
import os
import logging
import random
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

    @tasks.loop(hours=1)
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
                
@client.event                
async def on_message(message):
    # List of 89 different xeno groups, factions, names and nametypes (singular and plural!)
    xenos_races = ["necron","necrons","szarekhan","sautekh","mephrit","nihilakh","novokh","thokt","ogdobekh","nekthyst","maynarkh","t\'au","vior\'la","sa\'cea","dal\'yth","bork\'an","farsight enclaves","kel\'shan","au\'taal","ke\'lshan","vash\'ya","d\'yanoi","tau\'n","mu\'gulath bay","fal\'shia","ksi\'m\'yen","tash\'var","t\'ros","elsy\'eir","tau","viorla","sacea","dal\'yth","borkan","kelshan","autaal","kelshan","vashya","dyanoi","taun","falshia","ksimyen","tashvar","tros","elsyeir","aeldari","eldar","drukhari","alaitoc","biel-tan","iyanden","ulthwé","saim-hann","ynnari","harlequins","exodites","kroot","vespid","nicassar","demirg","tarellians","gue\'vesa","guevesa","goffs","deathskulls","snakebites","freebooterz","gretchin","ork","orc","orkz","orcs","orks","orcz","leviathan","kraken","behemoth","hydra","jormungandr","kronos","gorgon","tiamet","tyranid","tyranids","nid","nids","corsairs","corsair","tarellian"]    
    punctuation_chars = '.,!?;:()[]{}"'  # Add any additional punctuation characters you want to remove
    words = [word.strip(punctuation_chars) for word in message.content.lower().split()]
    if message.author == client.user:
        return

    if any(word in xenos_races for word in words):
        # 100 Imperial quotes about slaughtering xenos
        # You really should keep this closed untill I figure out a better way to do this :)
        xeno_quotes = [
            "In the grim darkness of the far future, there is only xenos to exterminate.",
            "Xenos filth, your annihilation is imminent!",
            "Purge the alien, for the Emperor\'s glory!",
            "For the Imperium, xenos scum shall know no mercy!",
            "In the Emperor\'s name, we cleanse the galaxy of xenos taint.",
            "Their heresy is xenos, their punishment is death!",
            "By the Emperor\'s will, we eradicate the alien threat.",
            "Xenos: the fuel for our righteous fury!",
            "Xenos presence detected, commence the cleansing!",
            "Let none survive. Purge the xenos from our midst!",
            "No quarter for xenos, only death!",
            "The xenos stain must be wiped from the galaxy.",
            "The Emperor\'s wrath shall cleanse the xenos scourge.",
            "Xenos blood shall flow like a river of righteousness.",
            "In our wake, only ashes and xenos corpses remain.",
            "We are the Emperor\'s sword, and the xenos are our prey.",
            "The xenos threat is a blight upon the galaxy, and we are the cure.",
            "Xenos may breed, but we shall cleanse.",
            "Their kind shall know only extinction at our hands.",
            "Xenos, your existence is an affront to the Imperium.",
            "To purge xenos is to honor the Emperor.",
            "The xenos are but insects before the might of the Imperium.",
            "We are the instruments of xenos destruction.",
            "In the face of xenos, we stand unwavering.",
            "Xenos: the prey of the righteous hunter.",
            "The Emperor\'s judgment falls upon the xenos.",
            "The galaxy belongs to humanity, not xenos abominations.",
            "We are the fire that burns away the xenos plague.",
            "For every xenos slain, the Emperor smiles upon us.",
            "Xenos scum, your reckoning is at hand!",
            "In the darkest depths of the galaxy, we hunt the xenos.",
            "Purity is achieved through the cleansing of xenos taint.",
            "Xenos, your doom approaches on wings of fire.",
            "The xenos threat shall crumble before the Imperium\'s might.",
            "With faith and bolter, we shall vanquish the xenos.",
            "Xenos, your existence is a blight upon humanity.",
            "For the Imperium, we shall scour the galaxy of xenos abominations.",
            "The xenos threat is a cancer, and we are the cure.",
            "In the shadow of the Emperor, we smite the xenos.",
            "Xenos blood shall water the soil of our sacred worlds.",
            "We are the righteous fury that burns through xenos ranks.",
            "To purify the galaxy, we must first purge the xenos.",
            "Xenos, your time in this galaxy is at an end.",
            "In the Emperor\'s name, we cleanse the stars of xenos.",
            "Xenos shall be a forgotten memory, erased by our might.",
            "We are the vengeful hand of the Imperium, striking down xenos.",
            "Xenos, your doom approaches on wings of fire.",
            "The xenos threat shall crumble before the Imperium\'s might.",
            "With bolter and blade, we shall carve the xenos from existence.",
            "In the eternal war of the 41st millennium, only the xenos shall be purged.",
            "Xenos, beware the Emperor\'s wrath!",
            "Purge the unclean! Purge the xenos!",
            "Xenos die, so humanity may thrive!",
            "For the Imperium, for humanity, for xenos extinction!",
            "Xenos: our enemies, our prey, our death sentence!",
            "The xenos must fall, for the Emperor\'s glory!",
            "No xenos shall escape our righteous fury!",
            "Xenos, your existence is blasphemy!",
            "In the Emperor\'s name, we smite the xenos!",
            "Xenos, meet your doom in steel and fire!",
            "Xenos skulls for the Skull Throne!",
            "Death to xenos, death to the heretic!",
            "Purge the xenos threat with holy fire!",
            "We are the sword of humanity, xenos our quarry!",
            "For Terra, for the Emperor, for xenos annihilation!",
            "In the face of xenos, we are unwavering!",
            "Xenos, your fate is sealed in blood!",
            "Xenos, you are beneath our notice, but not our wrath!",
            "By the Emperor\'s grace, xenos shall fall!",
            "Xenos heretics, tremble before our might!",
            "The xenos must be purged to save the Imperium!",
            "Purge! Purge! Purge!",
            "For humanity\'s survival, we cleanse the xenos stain!",
            "Xenos, you are the fuel of our righteous anger!",
            "In unity, we smite the xenos scourge!",
            "With bolter and blade, we cleanse the galaxy!",
            "No mercy, no respite, only xenos death!",
            "Xenos, your presence sickens the galaxy!",
            "Xenos, your extinction is our mission!",
            "To be xenos is to be damned!",
            "Xenos, your fate is sealed in steel!",
            "Purity through xenos purging!",
            "Xenos: we are the cure for your plague!",
            "Xenos, you are nothing before the Imperium!",
            "For the Emperor and mankind, we purge xenos!",
            "Xenos blood stains the path to victory!",
            "For the Emperor\'s glory, we annihilate xenos!",
            "Xenos heresy ends in death!",
            "With every xenos slain, humanity triumphs!",
            "Purge the xenos, cleanse the galaxy!",
            "Xenos, your resistance is futile!",
            "For the Emperor\'s honor, we strike down xenos!",
            "Xenos, your lives are forfeit!",
            "To purge xenos is to be truly human!",
            "Xenos: the enemies of mankind!",
            "For the Emperor\'s sake, we hunt the xenos!",
            "In the Emperor\'s name, we obliterate the xenos!",
            "Xenos, you are but a stain upon the galaxy!",
            "Xenos, face the wrath of the righteous!",
            "Xenos abominations, your end is nigh!"]
        random_number = random.randint(0,99)
        await message.channel.send(xeno_quotes[random_number])           
                
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