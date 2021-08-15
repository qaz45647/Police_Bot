# Discord_Bot - 支語警察機器人

![https://truth.bahamut.com.tw/s01/202108/c61d64f20c8e88f03d4d9e9ec8b793cb.JPG](https://truth.bahamut.com.tw/s01/202108/c61d64f20c8e88f03d4d9e9ec8b793cb.JPG)

## 主功能：

機器人會偵測每次傳送的訊息中是否提到關鍵字，如果提到會發訊息提醒，並加入違規清單![https://media.discordapp.net/attachments/870613188046110771/875743134598979664/IMG08.png](https://media.discordapp.net/attachments/870613188046110771/875743134598979664/IMG08.png)

如果違規清單出現重複用戶3次，會給該用戶"囚犯"身分組，並到公告頻道通知

![https://cdn.discordapp.com/attachments/870613188046110771/875760913901297674/IMG012.png](https://cdn.discordapp.com/attachments/870613188046110771/875760913901297674/IMG012.png)

![https://media.discordapp.net/attachments/870613188046110771/875759794718404698/IMG014.png](https://media.discordapp.net/attachments/870613188046110771/875759794718404698/IMG014.png)

懲罰時間結束後，機器人會移除你的"囚犯"身份組，並到公告頻道通知

![https://media.discordapp.net/attachments/870613188046110771/875760566138966067/IMG015.png](https://media.discordapp.net/attachments/870613188046110771/875760566138966067/IMG015.png)

## 指令：

### [公告頻道 頻道id

設定公告頻道的id，機器人會在這裡發佈通知

![https://media.discordapp.net/attachments/870613188046110771/875743119310721024/IMG02.png](https://media.discordapp.net/attachments/870613188046110771/875743119310721024/IMG02.png)

### [囚犯身分組 囚犯身分組id

設定囚犯身分組的id，違規用戶會被賦予此身分組

![https://media.discordapp.net/attachments/870613188046110771/875743123752484904/IMG03.png](https://media.discordapp.net/attachments/870613188046110771/875743123752484904/IMG03.png)

### [違規次數 數字

修改機器人判定入獄的違規次數

![https://media.discordapp.net/attachments/870613188046110771/875743126491394058/IMG04.png](https://media.discordapp.net/attachments/870613188046110771/875743126491394058/IMG04.png)

### [刑期 數字

修改違規用戶維持"囚犯"身分組的時間

單位：秒s

![https://media.discordapp.net/attachments/870613188046110771/875743128664018994/IMG05.png](https://media.discordapp.net/attachments/870613188046110771/876417346397413426/-1.png)

### [支語清單

顯示支語清單

![https://media.discordapp.net/attachments/870613188046110771/875743109462495232/IMG01.png?width=836&height=620](https://media.discordapp.net/attachments/870613188046110771/875743109462495232/IMG01.png?width=836&height=620)

### [新增支語 支語 正確用法

 新增關鍵字給機器人作判斷![https://media.discordapp.net/attachments/870613188046110771/875743130656313394/IMG06.png](https://media.discordapp.net/attachments/870613188046110771/875743130656313394/IMG06.png)

### [移除支語 支語 正確用法

移除指定關鍵字

![https://media.discordapp.net/attachments/870613188046110771/875743131348377680/IMG07.png](https://media.discordapp.net/attachments/870613188046110771/875743131348377680/IMG07.png)

### [我的違規次數

顯示使用者的違規次數與剩餘扣打

![https://media.discordapp.net/attachments/870613188046110771/875743134666067978/IMG09.png](https://media.discordapp.net/attachments/870613188046110771/875743134666067978/IMG09.png)

### [呼叫支語警察

隨機生成一張支語警察(共61張)

![https://media.discordapp.net/attachments/870613188046110771/875743137279139950/IMG010.png](https://media.discordapp.net/attachments/870613188046110771/875743137279139950/IMG010.png)

### [呼叫支語大隊長

叫出我們酷酷的支語大隊長

![https://media.discordapp.net/attachments/870613188046110771/875743088830709830/IMG01.gif](https://media.discordapp.net/attachments/870613188046110771/875743088830709830/IMG01.gif)

## 使用須知：

### 前置作業 – discord

建立好自己的機器人後，邀請到群組裡

在群組中建立"警察"身分組，並給機器人添加此身分組

除基本權限外，需額外給予：

 ■需給予"警察"身分組「管理身分組」的權限

 ■需給予"警察"身分組在「公告頻道」發言的權限

在群組中建立"囚犯"身分組

 ■自定義權限，如：關閉發送訊息、新增反應等

### 請注意警察身分組的排序，排序低的身分組無法對排序高的身分組進行任何變動

![https://media.discordapp.net/attachments/870613188046110771/876095711219949618/IMG017.png](https://media.discordapp.net/attachments/870613188046110771/876095711219949618/IMG017.png)

![https://media.discordapp.net/attachments/870613188046110771/876098974803701760/IMG018.png](https://media.discordapp.net/attachments/870613188046110771/876427326689259531/IMG018.png)

如果沒理解錯的話;;

### 前置作業 – 程式

將機器人的TOKEN放到json檔的bot_TOKEN中

`"bot_TOKEN":"your bot token"`

打開Bot.py 修改頻道與囚犯身分組ID

`channel_id = 867417685994242099`

`prisoner_id = 867416055366287361`

前置作業完成後，打開終端機就能運行了

如要讓機器人保持24小時在線，可參考[這支影片](https://youtu.be/UT1h9un4Cpo)的教學

## 其他注意事項：

■機器人關閉後，程式會停止運作，所以記得手動幫有"囚犯"身分組的使用者移除身分組

###### (不然他就只能永遠當囚犯了)

■一台機器人只能為一個伺服器服務

■機器人關閉後，使用指令加入、修改的參數會重置，所以建議在程式端修改完機器人再執行

■在機器人移除"囚犯"身分組前，如果手動移除"囚犯"身分組，以下程式還是會照常執行

`await asyncio.sleep(sleep)  #"sleep"秒後`

`await member.remove_roles(prisoner)  #移除囚犯身分組`

`await channel.send(item +"已從監獄中解放")  #公告`

 我太爛了，解決不了這個問題