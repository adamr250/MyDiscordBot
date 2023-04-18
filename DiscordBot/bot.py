
import discord, time, asyncio, pathlib, os, random
from datetime import datetime
from discord.ext import commands
#import time
#import asyncio


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
#client = discord.Client(intents=intents)

TOKEN = "[PRIVATE]"
channel_ID = 123456789 #[PRIVATE]


@bot.command()
async def ping(ctx):
    channel = bot.get_channel(channel_ID)
    await ctx.channel.send('pong')


@bot.command()
async def hello(ctx, s=None):
    if s == 'there':
        await ctx.send('General Kenobi')
    else:
        await ctx.send('No')

#shutdown bot
@bot.command(aliases=['close'])
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.close()


#send random image from "jp" folder
#command: >pop or >0_0
@bot.command(aliases=['0_0'])
async def pop(ctx):
    path = pathlib.Path(__file__).parent.resolve()
    file = random.choice(os.listdir(str(path) + "\\pop"))
    await ctx.send(file=discord.File(str(path) + "\\pop\\" + file))


#random image from "im" folder
@bot.command()
async def image(ctx):
    #get current path
    path = pathlib.Path(__file__).parent.resolve()
    #await ctx.send(file=discord.File(str(path) + "\\jp\\1.png"))
    file = random.choice(os.listdir(str(path) + "\\im"))
    await ctx.send(file=discord.File(str(path) + "\\im\\" + file))


@bot.listen()
async def on_message(message):
        # don't respond to ourselves
        #if message.author == self.user:
        #    return
        if message.content == 'ping':
            await message.channel.send('pong')

        if message.content == 'hello there':
            await message.channel.send('General Kenobi')
        if message.content == 'time':
            channel = bot.get_channel(channel_ID)
            await channel.send(time.strftime("%H") + ":" + time.strftime("%M"))


@bot.event
async def on_ready():

    print("bot:user ready == {0.user}".format(bot))
    print("time module in use")
    while True:
        #send a message at a specific time
        current_hour = datetime.now().strftime("%H")
        if current_hour == "16":
            current_time = datetime.now().strftime("%H:%M")#hour %H min %M sec %S am:pm %p 
            if current_time == "16:30":
                await asyncio.sleep(1)
                #print("time module ended")
                channel = bot.get_channel(channel_ID)
                await channel.send("@here " + current_time)
                await asyncio.sleep(69) #nice
                break
            else:
                await asyncio.sleep(10)
        else:
            await asyncio.sleep(1800)

bot.run(TOKEN)
