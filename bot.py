import discord
from discord import voice_client
from discord.ext import commands
from youtube_dl import YoutubeDL
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from  discord . utils  import  get
from discord import FFmpegPCMAudio
import asyncio
import  time
import lxml
import os

bot = commands.Bot(command_prefix='j')

@bot.event
async def on_ready():
    print ( 'Log in with: ' )
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)
    
    
    
    if message.content.startswith("청소"):
        if message.author.guild_permissions.manage_messages:
            try:
                amount = message.content[6:]
                await message.channel.purge(limit=int(amount))
                await  message . channel . send ( f"** { amount } ** messages deleted." )
            except ValueError:
                await  message . channel . send ( "Please enter **number of messages to be cleaned." )
        else:
            await  message . channel . send ( "You do not have permission." )
    
@bot.command()
Enter async  def ( ctx ):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            embed = discord . Embed ( title = "[ Music ]" , description = "Hmm.. I'm not on that channel?" , color = 0x2bff00 )
            await ctx.send(embed=embed)

@bot.command()
get out async  def ( ctx ):
    try:
        await vc.disconnect()
    except:
        embed = discord . Embed ( title = "[ Music ]" , description = "Hmm.. I'm not on that channel?" , color = 0x2bff00 )
        await ctx.send(embed=embed)

@bot.command()
async  def playback ( ctx , * , url ):
    YDL_OPTIONS  = {' format ': ' bestaudio ', ' noplaylist ': ' True '}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await  ctx . send ( embed  =  discord . Embed ( title =  "Playing Song" , description  =  "Currently  playing " +  url  +  "" , color  =  0x00ff00 ))
    else:
        embed = discord . Embed ( title = "[ Music ]" , description = "Hmm.. I think music is playing" , color = 0x2bff00 )
        await ctx.send(embed=embed)
        
@bot.command()
async  def pause ( ctx ):
    if vc.is_playing():
        u . pause ()
        embed = discord . Embed ( title = "[ Music ]" , description = "You have finished pausing music" , color = 0x2bff00 )
        await ctx.send(embed=embed)
    else:
        embed = discord . Embed ( title = "[ Music ]" , description = "Music is not playing" , color = 0x2bff00 )
        await ctx.send(embed=embed)
        
@bot.command()
async  def replay ( ctx ):
    try:
        u . resume ()
    except:
        embed = discord . Embed ( title = "[ Music ]" , description = "No music in the pause list" , color = 0x2bff00 )
        await ctx.send(embed=embed)
    else:
        embed = discord . Embed ( title = "[ Music ]" , description = "Music replay completed" , color = 0x2bff00 )
        await ctx.send(embed=embed)

@bot.command()
async  def mute song ( ctx ):
    if vc.is_playing():
        u . stop ()
        embed = discord . Embed ( title = "[Music ]" , description = "Music Complete Turn Off Music" , color = 0x2bff00 )
        await ctx.send(embed=embed)
    else:
        embed = discord . Embed ( title = "[ Music ]" , description = "No music playing" , color = 0x2bff00 )
        await ctx.send(embed=embed)
        
bot . run ( 'your token')
