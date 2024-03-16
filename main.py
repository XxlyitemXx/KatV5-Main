import configs.config as config
import utils.discordutils as Util
import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="$",intents=intents,help_command=None)

@bot.event
async def on_ready():
    print("bot ready!")
    await bot.change_presence(activity=discord.Streaming(name="KatV5", url=config.TWITCH_CHANNEL))

@bot.run(config.DISCORD_TOKEN)