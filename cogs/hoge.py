import discord
from discord.ext import commands

class hoge(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """ボットにPINGを送ります。"""
        await ctx.send('hogehoge')
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content.startswith('/'):
            await message.channel.send(message.content)

def setup(bot):
    bot.add_cog(hoge(bot))
