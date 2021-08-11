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


#增減清單
#列出清單



violations_nb = 3       #違規次數
channel_id = 867417685994242099     #公告頻道id
prisoner_id = 867416055366287361        #"囚犯"身分組id



@bot.command()          #機器人Ping
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)} ms")

@bot.command()      #[修改公告頻道 867417685994242099
async def 公告頻道(ctx,msg):
    global channel_id
    channel_id = int(msg)
    await ctx.send("修改完成")

@bot.command()      #[修改囚犯身分組 867416055366287361
async def 囚犯身分組(ctx,msg):
    global prisoner_id
    prisoner_id = int(msg)
    await ctx.send("修改完成")

@bot.command()      #修改違規行為的扣打
async def 違規次數(ctx,msg):
    global violations_nb
    violations_nb = int(msg)
    await ctx.send(f"修改完成,違規次數為{violations_nb}次")

@bot.command()      #列出支語清單 print('{:^10}'.format('test'))
async def 支語清單(ctx):
    x=0
    y=0
    result=''
    list = jdata['tw_term']
    for item in jdata['cn_term']:
        space = 5-len(jdata['cn_term'][y])
        list.insert(x,jdata['cn_term'][y])
        result =result+list[x]+space * '　'+list[x+1]+'\n'
        x+=2
        y+=1
    await ctx.send(f"支語　　　正確用法\n{result}")

@bot.command()      #新增支語到清單中
async def 新增支語(ctx,msg1,msg2):
    jdata['cn_term'].append(msg1)
    jdata['tw_term'].append(msg2)
    await ctx.send(f"{jdata['cn_term']}\n{jdata['tw_term']}")

@bot.command()      #移除清單中的支語
async def 移除支語(ctx,msg1,msg2):
    jdata['cn_term'].remove(msg1)
    jdata['tw_term'].remove(msg2)
    await ctx.send(jdata['cn_term'])
    await ctx.send(jdata['tw_term'])

@bot.command()          #列出警告次數
async def 我的違規次數(ctx):    
    member = ctx.author.name
    nb = jdata['violation_list'].count(member)
    await ctx.send(f"你的違規次數為{nb}次,剩{violations_nb-nb}次扣打")

@bot.command()          #隨機生成一張支語警察圖片
async def 呼叫支語警察(ctx):    
    await ctx.send(jdata['pic']+pic_rd(5)+'.jpg')

@bot.command()          #召喚支語大隊長
async def 呼叫支語大隊長(ctx):    
    await ctx.send("https://upload.cc/i1/2021/08/08/YcCeSR.gif")

@bot.event      
async def on_message(msg):
    if msg.author != bot.user:      
        channel = bot.get_channel(channel_id)

        msg_author=msg.author.name
        violation = False
        term_index = -1

        for term in jdata['cn_term']:       #檢查訊息中是否有支語,有則列印出支語與其對應文字,並判定違規
            term_index += 1            
            if term in msg.content:
                await msg.channel.send(term +'❌→ ' + jdata['tw_term'][term_index]+'⭕')
                violation=True

        if violation == True:       #如果違規,會在機器人提醒後,張貼隨機支語警察圖片,並將使用者列入違規名單中
            await msg.channel.send(jdata['pic']+pic_rd(5)+'.jpg')
            jdata['violation_list'].append(msg_author)      

        for item in (jdata['violation_list']) :      #如果在違規名單中出現三次,清除清單紀錄,並增加"囚犯"身分
            if jdata['violation_list'].count(item) >=violations_nb:
                for a in range(violations_nb):
                    jdata['violation_list'].remove(item)

                guild = msg.guild
                prisoner = guild.get_role(prisoner_id)
                member = msg.author
                await member.add_roles(prisoner)
                await channel.send(item + "因違規被關入監獄5秒")                

                async def interval():       #5秒後清除"囚犯"身分  604800  #bug 刪除身分組 還是會執行                           
                    A_Car = True
                    if A_Car == True:
                        await asyncio.sleep(10)
                        await member.remove_roles(prisoner)
                        await channel.send(item +"已從監獄中解放")
                        A_Car = False
                bg_task = bot.loop.create_task(interval())

    await bot.process_commands(msg)
            
bot.run(jdata['bot_TOKEN'])