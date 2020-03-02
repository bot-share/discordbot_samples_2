#discordのライブラリをインポート
import discord
from discord.ext import commands

# 接続に必要なオブジェクトを作る
bot = commands.Bot(command_prefix='/')

token = 'THi5IsDuMMyaCCesSTOK3nQ4.Cl2FMQ.ThIsi5DUMMyAcc3s5ToKen7kKWs'

#BOTが起動したとき
@bot.event
async def on_ready():
    print('起動しました！(\'◇\')ゞ')

#ping コマンド
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def msg(ctx,*,msg):
  await ctx.send(msg)

if __name__ == '__main__':
    bot.run(token)
