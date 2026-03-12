import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Olá! Meu Nome é Erick Garcia, Eu amo o aspas e me casaria com ele e o neymar, meu sonho é ser radiante, mas não consigo, atualmente sou Ascendente, e sou fã do neymar')
@bot.command()
async def roll(ctx, dice: str):
    """Rola um dado no formato NdN (ex: 2d6)"""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Formato inválido! Use algo como 2d6')
        return

    results = [random.randint(1, limit) for r in range(rolls)]
    await ctx.send(', '.join(map(str, results)))

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

bot.run("SEU TOKEN")
