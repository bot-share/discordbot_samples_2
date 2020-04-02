#discordのライブラリをインポート
import discord
from discord.ext import commands
#cogsのhogeをimport
import cogs.hoge as hoge
# 接続に必要なオブジェクトを作る
bot = commands.Bot(command_prefix='!')

token = 'THi5IsDuMMyaCCesSTOK3nQ4.Cl2FMQ.ThIsi5DUMMyAcc3s5ToKen7kKWs'

#BOTが起動したとき
@bot.event
async def on_ready():
    #hogeのコグをロード
    hoge.setup(bot)
    print('起動しました！(\'◇\')ゞ')

#ping コマンド
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#!msg ~~ と打った時にそのメッセージをそのまま返す
@bot.command()
async def msg(ctx,*,msg):
    #BOTは無視
    if ctx.author.bot:
        return
    await ctx.send(msg)

#BOTを起動
if __name__ == '__main__':
    bot.run(token)
