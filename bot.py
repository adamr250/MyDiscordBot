
import discord, time, asyncio, pathlib, os, random
from os.path import exists;
from datetime import datetime
from discord.ext import tasks, commands
from setup import *;
from TwitchFollowedList import *;


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
#client = discord.Client(intents=intents)

config_object = ConfigParser()

if not exists('config.ini'):
    print("Running setup.")
    runSetup()

config_object.read("config.ini")

config = config_object["bot_config"]
TOKEN = config["bot_token"]
channel_id = int(config["channel_id"])

config = config_object["twitch_api_config"]
client_id = config["client_id"]
client_secret = config["client_secret"]
access_token = config["access_token"]
user_id = config["user_id"]


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


#send random image from "pop" folder
#command: >pop or >0_0
@bot.command(aliases=['0_0'])
async def pop(ctx):
    path = pathlib.Path(__file__).parent.resolve()
    file = random.choice(os.listdir(str(path) + "\\pop"))
    await ctx.send(file=discord.File(str(path) + "\\pop\\" + file))


#random image from "im" folder
@bot.command()
async def im(ctx):
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


@bot.command()
@commands.is_owner()
async def twitch_list(ctx):
    twitch_list = getTwitchFollowedList(client_id, client_secret, access_token, user_id);
    await ctx.channel.send(twitch_list)


#shutdown bot
@bot.command(aliases=['shutdown'])
@commands.is_owner()
async def close(self):
    try:
        await self.bot.close()
    except Exception:
        pass
    #print("Bot Closed")
    #sys.exit(0)

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
    
if __name__ == "__main__":
    bot.run(TOKEN)
