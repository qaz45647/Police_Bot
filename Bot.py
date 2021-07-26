import discord
from discord import file
from discord.ext import commands
import json
import random


def pic_rd(length):         #隨機生成一個字串
    prd = str()
    characters = "qwertyuiopasdfghjklzxcvbnm" + "1234567890"
    for i in range(length):
        prd = prd +  random.choice(characters)
    return prd

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")


@bot.command()          #機器人Ping
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)} ms")


@bot.command()          #隨機生成一張支語警察圖片
async def Police_IMG(ctx):    
    await ctx.send(jdata['pic']+pic_rd(5)+'.jpg')

@bot.event      #判斷是否有支語
async def on_message(msg):    
    term_index = -1    
    for term in jdata['cn_term']:
        term_index = term_index + 1            
        if term in msg.content and msg.author != bot.user:            
            await msg.channel.send(term + jdata['tw_term'][term_index]) 
        #await msg.channel.send(jdata['pic']+pic_rd(5)+'.jpg')            


bot.run(jdata['Bot_TOKEN'])