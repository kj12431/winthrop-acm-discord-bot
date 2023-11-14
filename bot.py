import discord
from discord.ext import commands
import random

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

@bot.command()
async def hello(ctx):
    await ctx.send('hi there')

#=====================================================

tycoon = 0
#create cards function here

@bot.command(name='start_tycoon')
async def start_game(ctx, *players: discord.User):
    tycoon = 1

#=====================================================

@bot.command(name='play_card')
async def play_card(ctx):
    if tycoon == 1:
        pass
    

bot.run(DISCORD_TOKEN)
