import discord
from discord.ext import commands

import os 

from dotenv import load_dotenv
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('hi there')

# Logic goes here

bot.run(DISCORD_TOKEN)
