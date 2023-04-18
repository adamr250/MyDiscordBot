
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first
import asyncio


import sys, json;
import requests;
from os.path import exists;
from configparser import ConfigParser;

client_id = '[PRIVATE]'
client_secret = '[PRIVATE]'
access_token = '[PRIVATE]'
user_id = '[PRIVATE]'

# Define headers
headers = {
    'Authorization': 'Bearer ' + access_token, #keys['access_token'],
    'Client-ID': client_id
}


response = requests.get('https://api.twitch.tv/helix/streams/followed?user_id=' + user_id, headers=headers)

data = response.json()
numStreams = len(data["data"])

print ("\nCHANNEL " + ' '*13 + "GAME" + ' '*37 + "VIEWERS" + ' '*8 + "\n" + '-'*80)


for i in range (0, numStreams):
    channelName = data["data"][i]["user_name"];
    channelGame = data["data"][i]["game_name"];
    channelViewers = str(data["data"][i]["viewer_count"]);
    streamType = data["data"][i]["type"];

    # Check if stream is actually live or VodCast
    if(streamType == "live"):
        streamType = "";
    else:
        streamType = "(vodcast)";

    #Truncate long channel names/games
    if(len(channelName) > 18):
        channelName = channelName[:18] + ".."
    if(len(channelGame) > 38):
        channelGame = channelGame[:38] + ".."

    #Formatting
    print ("{} {} {} {}".format(
	channelName.ljust(20),
	channelGame.ljust(40),
	channelViewers.ljust(8),
	streamType
    ))

print ('-'*80)
