import discord
from discord.ext import commands
from config import TOKEN
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


# Dönüştürülen Discord kütüphane dosyasınini saklama
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


# duck komutunu çağırdığımızda, program
# ordek_resmi_urlsi_al fonksiyonunu çağırır
@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run(TOKEN)
