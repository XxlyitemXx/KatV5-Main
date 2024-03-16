import configparser
config = configparser.ConfigParser()
config.read('config.ini')
DISCORD_OWNER_ID = config['MAIN']['discord_owner_id']
DISCORD_TOKEN = config['MAIN']['discord_bot_token']
GEMINI_APIKEY = config['MAIN']['gemini_api_key']
ON_REMOVE_CHANNEL = config['MAIN']['on_member_remove_channel']
ON_JOIN_CHANNEL = config['MAIN']['on_member_join_channel']
TWITCH_CHANNEL = config['MAIN']['twitch_channel']
