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
async def on_message(message):
    if message.author == bot.user: 
        return
    if message.content.startswith("!help"):
        await message.channel.send("Check Your DM!")
        member = message.author
        dm = await member.create_dm()
        await dm.send(f"idk")

@bot.event
async def on_ready():
    print("bot ready!")
    await bot.change_presence(activity=discord.Streaming(name="KatV5", url=config.TWITCH_CHANNEL))
@bot.event
async def on_member_join(member):
    print("New Member Joining")
    members = member.mention
    guild = member.guild
    guildname = guild.name
    Channel = bot.get_channel(config.ON_JOIN_CHANNEL)
    Channel.send(f" Welcome to Our Server!, {members}")
    dm = await member.create_dm()
    await dm.send(f"Welcome To {guildname}!")
@bot.event
async def on_member_remove(member):
    print("sm1 left the server")
    channel = bot.get_channel(config.ON_REMOVE_CHANNEL)
    members = member.mention
    await channel.send(f"GoodBye {members} We Hope, we will see you again!")






@bot.run(config.DISCORD_TOKEN)