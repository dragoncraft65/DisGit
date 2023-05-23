import os

import discord


def make_repos_folder():
    if os.path.exists("DisGit_Repos"):
        print("DisGit Repo folder already made")
    else:
        os.mkdir("DisGit_Repos")
        print("DisGit Repo folder has been created")


def disgit_help_function():
    embed = discord.Embed(title="DisGit Help")
    embed.add_field(name= "git -h", value = "You got to this menu so you must know how to use it")
    return embed

async def disgit_message_handler(message, client):
    if message.author == client.user:
        return

    elif message.content.split()[0] == "git":
        if len(message.content.split()) == 1:
            await message.channel.send("Run git -h to access the help menu if you don't know what your doing")
            return
        elif message.content.split()[1] == "-h":
            await message.channel.send(embed=disgit_help_function())
    else:
        return