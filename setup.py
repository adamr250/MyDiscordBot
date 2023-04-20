from configparser import ConfigParser

def runSetup():
    config_object = ConfigParser()

    bot_token = input("Enter your bot token: ");
    channel_id = input("Enter channel id: ");

    user_id = input("Enter twitch user id: ");
    client_id = input("Enter your client id: ");
    client_secret = input("Enter your client secret: ");
    access_token = input("Enter your access token: ");

    config_object["bot_config"] = {
        "bot_token": bot_token,
        "channel_id": channel_id
    }

    config_object["twitch_api_config"] = {
        "user_id": user_id,
        "client_id": client_id,
        "client_secret": client_secret,
        "access_token": access_token
    }

    with open('config.ini', 'w') as conf:
        config_object.write(conf);
