import discord
from discord.ext import commands
from tokens_boxuga import *
from main_functions import messagewebpage

bot = commands.Bot(command_prefix='$')
myStatus = 'Changing Site'

@bot.event
async def on_ready():
        print('We have logged in as {0.user}'.format(bot))
        await bot.change_presence(activity=discord.Game(myStatus)) 

@bot.command()
async def me(ctx, *, msg):
    messagewebpage(msg, "__" + ctx.author.name + "#" + str(ctx.author.discriminator) + "__", ctx.author.avatar_url)
    await ctx.send('Message Sent')


bot.run(discord_bot_token)