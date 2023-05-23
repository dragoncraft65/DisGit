# Discord bot that acts like a private GitHub account
# Needs discord.py to be installed

# This is a dumb project ment to be used for memes with friends and is not good for storing importent files


# Imports
import discord
import asyncio
from client_funcs import *

def main():
    client = generate_client()

    @client.event
    async def on_message(message):
        if message.author != client.user:
            await message.channel.send(message.content)

if __name__ == "__main__":
    main()



