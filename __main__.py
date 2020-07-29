# do not skid
import discord
from discord.ext import commands
from discord.ext.commands import Bot

token = ""
prefix = "plsstart!"

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Ready to spam the fuck out of 'pls beg'")
    print('Created by ZinX, all code by ZinX')

@bot.command(pass_context=True)
async def start(ctx):
    if bot.user.id == ctx.message.author.id:
      while True:
        await ctx.send('pls beg')
        await asyncio.sleep(60)

#pls!start command

bot.run(token, bot=False)
