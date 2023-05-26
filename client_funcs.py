# Functions that create and modify the client


# Imports
import discord
import requests

# builds a discord client with all the intents needed for the bot
def generate_client():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.guilds = True
    intents.members = True
    client = discord.Client(intents=intents)
    return client

# loads the token from a file path
def get_token(fp):
    with open(fp, "r") as f:
        token = f.read()
    return token


# Takes in url and path and downloads; this is why there is no security
def file_from_url(fp, url):
    unfiltered = requests.get(url)
    content = str(unfiltered.content)
    with open(fp, "w") as f:
        f.write(content)