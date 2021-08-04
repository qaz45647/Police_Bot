from inspect import EndOfBlock
import discord
from discord import file
from discord import message
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
async def 呼叫支語警察(ctx):    
    await ctx.send(jdata['pic']+pic_rd(5)+'.jpg')

@bot.event      
async def on_message(msg):
    if msg.author != bot.user:      #檢查訊息中是否有支語,有則列印出支語與其對應文字,並判定違規
        violating_Users=msg.author.name
        violation = False   
        term_index = -1    
        for term in jdata['cn_term']:
            term_index += 1            
            if term in msg.content:          
                await msg.channel.send(term +'❌→ ' + jdata['tw_term'][term_index]+'⭕')
                violation=True

        if violation == True:       #如果違規,會在機器人提醒後,張貼隨機支語警察圖片,並將使用者列入違規名單中.
            await msg.channel.send(jdata['pic']+pic_rd(5)+'.jpg')
            jdata['violation_list'].append(violating_Users)
            print(jdata['violation_list'])
            
            
    await bot.process_commands(msg)
    


    #await msg.channel.send(jdata['pic']+pic_rd(5)+'.jpg')            



bot.run(jdata['bot_TOKEN'])