import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='1')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run("ODY3MDM4MTczMzg5NzgzMDcx.YPbSOQ.2QQvRhpORiAG5bSJNzKIAyNnUDA")