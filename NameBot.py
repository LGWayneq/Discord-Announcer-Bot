import os
import nest_asyncio
from discord.ext import commands
import discord
from dotenv import load_dotenv

nest_asyncio.apply()
load_dotenv()
TOKEN = "ODY5ODg5NDc5NDgwMDY2MTA4.YQExtQ.6YtohaCfF0yyQ5Q3kPd6kkVloMU"
GUILD = "MAFPOVBUL"

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name = GUILD)
    print(
        f'{bot.user} is connected to the following guild: \n'
        f'{guild.name} (id: {guild.id})')
    
@bot.event
async def on_voice_state_update(member,before,after):
    guild = discord.utils.get(bot.guilds, name = GUILD)
    if member.bot:
        return
    if before.channel == None and after.channel:
        if member.voice:
            await guild.text_channels[0].send(content = member.name, tts = True, delete_after = 5)
            #await member.voice.channel.connect()
    elif after.channel == None and before.channel:
        await guild.text_channels[0].send(content = f"{member.name} left", tts = True, delete_after = 5)
        #if bot.voice_clients:
            #await bot.guilds[0].voice_client.disconnect()

"""@bot.event
async def on_message(message):
    print(message.author)
    print(bot.user)
    if message.author == bot.user:
        bot.delete_message(message)"""

bot.run(TOKEN)
