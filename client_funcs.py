# Functions that create and modify the client


# Imports
import discord

def generate_client():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.guilds = True
    intents.members = True
    client = discord.Client(intents=intents)
    return client