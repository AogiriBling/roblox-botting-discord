import os
from discord.ext import commands 
import discord, requests, random, threading, asyncio
from webserver import keep_alive

with open('Bling.txt', 'r') as cookies:
    cookies1 = cookies.read().splitlines()

bot = commands.Bot(command_prefix='.')

token = ''

@bot.event
async def on_ready():
 members = sum([guild.member_count for guild in bot.guilds])
 await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Aogiri Tree"))
 print("Members")

def add_user(cookie, userid):
    try:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
            session.post(f'https://friends.roblox.com/v1/users/{userid}/request-friendship')
    except:
        pass



@bot.command()
async def rfriend(ctx, userId):
            embed = discord.Embed(color=0x0F0F0F, description=f"**__* <@{ctx.author.id}> Sent*__** `60` **__*Friend Requests*__**")
            await ctx.send(embed=embed)
            for x in cookies1:
                threading.Thread(target=add_user, args=(x, userId,)).start()



def follow_user(cookie, userid):
    try:
        with requests.session() as session:
             session.cookies['.ROBLOSECURITY'] = cookie
             session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
             session.post(f'https://friends.roblox.com/v1/users/{userid}/follow')
    except:
        pass


@bot.command()
async def rfollow(ctx, userId):
            embed = discord.Embed(color=0x0F0F0F, description=f"**__*<@{ctx.author.id}> Sent*__** `45` **__*Followers*__** `[BETA]`")
            await ctx.send(embed=embed)
            for x in cookies1:
                threading.Thread(target=follow_user, args=(x, userId,)).start()


bot.run(token)
