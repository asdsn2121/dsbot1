import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def bye(ctx):
    await ctx.send(f'bye {ctx.message.author} ')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} Зашёл на сервер {discord.utils.format_dt(member.joined_at)}')
