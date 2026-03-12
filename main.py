import requests
import os
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

@bot.command()
async def meme(ctx):
    memes = os.listdir("images")

    raridades = []
    tipos = []

    for meme in memes:
        if "lendario" in meme:
            raridades.append(1)
            tipos.append("lendario")
        elif "epico" in meme:
            raridades.append(3)
            tipos.append("epico")
        elif "raro" in meme:
            raridades.append(6)
            tipos.append("raro")
        else:
            raridades.append(10)
            tipos.append("comum")

    escolha_index = random.choices(range(len(memes)), weights=raridades, k=1)[0]
    img = memes[escolha_index]
    tipo = tipos[escolha_index]

    with open(f'images/{img}', 'rb') as f:
        picture = discord.File(f)

    if tipo == "lendario":
        await ctx.send(" W MEME LENDÁRIO ENCONTRADO!")
    elif tipo == "epico":
        await ctx.send(" MEME ÉPICO SUPER FUNNY!")

    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)



bot.run("Seu Token")
