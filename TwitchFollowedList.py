
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first

import asyncio
import sys, json;
import requests;
from os.path import exists;
from configparser import ConfigParser;

def getTwitchFollowedList(client_id, client_secret, access_token, user_id):

    # Define headers
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Client-ID': client_id
    }

    #Get data about followed accounts
    response = requests.get('https://api.twitch.tv/helix/streams/followed?user_id=' + user_id, headers=headers)

    data = response.json()
    numStreams = len(data["data"])


    #print ("\nCHANNEL " + ' '*13 + "GAME" + ' '*37 + "VIEWERS" + ' '*8 + "\n" + '-'*80)
    twitch_list = "\nCHANNEL " + ' '*13 + "GAME" + ' '*37 + "VIEWERS" + ' '*8 + "\n" + '-'*80 + "\n";

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
        twitch_list = twitch_list + ("{} {} {} {}".format(
	    channelName.ljust(20),
	    channelGame.ljust(40),
	    channelViewers.ljust(8),
	    streamType
        ))
        twitch_list = twitch_list + "\n"

    #print ('-'*80)
    twitch_list = twitch_list + '-'*80
    #print(twitch_list)
    return twitch_list;
