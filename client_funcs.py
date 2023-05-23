# Functions that create and modify the client


# Imports
import discord

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

def