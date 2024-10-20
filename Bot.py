from inspect import EndOfBlock
import discord
from discord import file
from discord import message
from discord import guild
from discord import member
from discord import user
from discord import channel
from discord.ext import commands
import json,asyncio
import random


"""
-.`                            `-+yhhhhhhhhhyo+-`                    `..`.-
`                          ` -+ydddddhddddshddh/`                         `
.                        `:shddddddhs:ohdy/++/sddo` `                     `
-                     -/yddddddddddyo//sdy+os//yddh/ `                    `
:                `./shddddddddddddddo/+sdh++s+/sddddy-                    `
:             .:shhdddddddddddddddhs++yhddhyyoshdddddd+`                  `
:         `./shddddddddddddddddddds+/:/yddo++o++hddddddh-                 `
:       ./yddddddddddddddddddddddddy+/sdddy//+oydddddddddo.               `
:     -oddddddddddddddddddddddddddddyooddsss+yssydddddddddh-              `
:   :ymdddddddddddddddddddddddddmmmmmddNNmmmhddmmmddddddddddo`            `
-  omdddddddddddddddddddmmmNNNMMMMMMshyNy/:+//doNMMNmddddddddh-           `
: /NddddddddddddmmmNNNMMMMMMMMMMMMMNsdss-+:oo/shMMMMMMNdddddddd:          `
- /mdddddmmmNNMMMMMMMMMMMMMMMMMMMMMMMMMdo:h/h/sshNMMMMMMmddddddd.         `
:  -symdmMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhsyo/ooddhdhyhMMMMMMmddddy.         `
:     ..oNMMMMMMMMMMMMMMMMMMMMMMMMMMMNos+syMMMMNyyoNMMMMMMMNyo.`          `
:        hMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNmmdddmdddmNNNd`             `
:      `:yNNNNmmdmdhhdyyyyyhyydyydyshyssyooshooosooossoodohy.             `
:      `hshyyyyyyy+////+oossyyhhhdddddddddddddddddddddddddddhy:`          `
:       -:/hyyyyyy+`````:.`....--://+oyo+++++yddhddddddddhhddddh+.        `
:       `.sosyyyyhh-```.+`.:++oosssyyyyh-````ohyyyssssyhds:-:+yyhy+       `
:        -+.:+oshys.````.`-/////++++ooo:``````:o+oooossyh:     ````       `
:        -+::-/ohh:```````-/syyyssssyys/````--/+.+osyhhs//                `
:        -o:+-/:sd.`.```````````````````````-y-``````````.                `
:        `y.o`o/:y``+..``````````````````````-y/`````````+.               `
:         /s:..:+/``.:-.``````````````````````.os.```````s-               `
:          .:+o/`.``````````````````````:-``````y/``````.h                `
:         `   //`-.`````````````````````s.-//-`:h.``````o/                `
:            `s:`./`````````````````````..````-s-``````.y                 `
:           `/d.``+.```````````````````````````````````s-                 `
:          /ydd.``::```````````````````````````./:````/+                  `
:        -sddmy```.//-```````````````:++++++++/-/-```-o                    
:       :hdmmm/````-/:/:.````````````-:::+oso/::````-s`                    
: `.-:/ohdddmd-`````:-.:/:.```````````-:-...-:/-```.h+                     
osyhddddddddddh+.````/.``-//-`````````````````````.hddo-`                  
ydddddddddddddddy/.``./.```-//-.`````````````````.ydddddd:                `
ydddddddddddddddddy:.`./`````.:::.```````````````:dddddddd.                
ydddddddddddddddddddy/.:/```````.--:://://///+oosyddddmddmdo:.             
yddddddddddmdddddddddddhd+.`````````````.s.``odddddddmddddmmddy+- `        
shhhhhhhhhhhhhhhhhhhhhhhhhy.```````````-s+```yhhhhhhhdhhhhhhhhhhhyo:``   ``
"""


with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='[')

####################################################
#使用前需先修改channel_id、prisoner_id與json中的"bot_TOKEN"
channel_id = 867417685994242099     #公告頻道id
prisoner_id = 867416055366287361        #"囚犯"身分組id
####################################################

sleep = 300       #入獄時間(s)
violations_nb = 3       #違規次數


@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.command()          #機器人Ping
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)} ms")

@bot.command()      #修改公告頻道 
async def 公告頻道(ctx,msg):
    global channel_id
    channel_id = int(msg)
    await ctx.send("修改完成")

@bot.command()      #修改囚犯身分組 
async def 囚犯身分組(ctx,msg):
    global prisoner_id
    prisoner_id = int(msg)
    await ctx.send("修改完成")

@bot.command()      #修改違規行為的扣打
async def 違規次數(ctx,msg):
    global violations_nb
    violations_nb = int(msg)
    await ctx.send(f"修改完成,違規次數為{violations_nb}次")

@bot.command()      #修改囚犯身分組的刑期
async def 刑期(ctx,msg):
    global sleep
    sleep = int(msg)
    await ctx.send(f"修改完成,刑期為{sleep}秒")

@bot.command()      #列出支語清單 
async def 支語清單(ctx):
    x=0
    result=''
    list = []
    list += jdata['tw_term']
    for item in jdata['cn_term']:
        space = 5-len(item)
        list.insert(x,item)
        result = result + list[x] + space * '　' + list[x+1] + '\n'
        x += 2
    await ctx.send(f"支語　　　正確用法\n{result}")    


@bot.command()      #新增支語到清單中
async def 新增支語(ctx,msg1,msg2):
    if msg1 in jdata['cn_term']:
        await ctx.send('關鍵字已在清單中,新增無效!')
    elif msg2 in jdata['tw_term']:
        await ctx.send('關鍵字已在清單中,新增無效!')
    else:
        jdata['cn_term'].append(msg1)
        jdata['tw_term'].append(msg2)
        await ctx.send(f"已新增{msg1}、{msg2}到清單中")

@bot.command()      #移除清單中的支語
async def 移除支語(ctx,msg1,msg2):
    if msg1 not in jdata['cn_term']:
        await ctx.send('您要刪除的關鍵字並不在清單中...')
    elif msg2 not in jdata['tw_term']:
        await ctx.send('您要刪除的關鍵字並不在清單中...')
    else:    
        jdata['cn_term'].remove(msg1)
        jdata['tw_term'].remove(msg2)
        await ctx.send(f"已從清單中移除{msg1}、{msg2}")

@bot.command()          #列出警告次數
async def 我的違規次數(ctx):    
    member = ctx.author.name
    nb = jdata['violation_list'].count(member)
    await ctx.send(f"你的違規次數為{nb}次,剩{violations_nb-nb}次扣打")

@bot.command()          #隨機生成一張支語警察圖片
async def 呼叫支語警察(ctx):    
    await ctx.send(random.choice(jdata['pic']))

@bot.command()          #召喚支語大隊長
async def 呼叫支語大隊長(ctx):    
    await ctx.send("https://upload.cc/i1/2021/08/08/YcCeSR.gif")

@bot.event      
async def on_message(msg):
    if msg.author != bot.user and msg.content[0] != '[':
        channel = bot.get_channel(channel_id)
        msg_author=msg.author.name
        violation = False
        term_index = -1
        result = ''
        for term in jdata['cn_term']:       #檢查訊息中是否有支語,有則將支語與其對應文字加入result中,violation=True
            term_index += 1            
            if term in msg.content:
                result = result + term +'❌→ ' + jdata['tw_term'][term_index]+'⭕' + '\n'
                violation=True

        if violation == True:       #如果violation=True,將result加上隨機支語警察圖片，並列印,將使用者列入違規名單中
            result = result + random.choice(jdata['pic']) + '\n'
            await msg.channel.send(result)
            jdata['violation_list'].append(msg_author)      

        for item in (jdata['violation_list']) :      #如果在違規名單中出現三次,清除清單紀錄,並增加"囚犯"身分
            if jdata['violation_list'].count(item) >=violations_nb:
                for a in range(violations_nb):
                    jdata['violation_list'].remove(item)

                guild = msg.guild
                prisoner = guild.get_role(prisoner_id)
                member = msg.author
                await member.add_roles(prisoner)
                await channel.send(f"{item}  因違規被關入監獄{sleep}秒")  
                                   
                await asyncio.sleep(sleep)      #"sleep"秒後清除"囚犯"身分   #bug 在刑期結束前移除"囚犯"身分組 程式還是會照常執行 
                await member.remove_roles(prisoner)       
                await channel.send(item +"已從監獄中解放")
             
    await bot.process_commands(msg)

bot.run(jdata['bot_TOKEN'])
