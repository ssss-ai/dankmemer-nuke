import discord, asyncio
from discord.ext import commands
from discord.ext.commands import Bot


token = ""100,000""
prefix = "plsstart!"

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Ready to spam 'pls beg' lol")
    print('Created by Cryptos1337. Give Credits if you\'re recording :)')

@bot.command(pass_context=True)
async def start(ctx):
    if bot.user.id == ctx.message.author.id:
      while True:
        await ctx.send('pls beg')
        await asyncio.sleep(60)

#plsstart!start

bot.run(token, bot=False)
