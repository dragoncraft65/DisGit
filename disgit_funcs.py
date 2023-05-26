# functions that work with the git thing

# Settings
ACCEPTED_FORMATS = ["py", "txt"]

# imports
import os
import discord
import shutil
from client_funcs import file_from_url
def make_repos_folder():
    if os.path.exists("DisGit_Repos"):
        print("DisGit Repo folder already made")
    else:
        os.mkdir("DisGit_Repos")
        print("DisGit Repo folder has been created")


async def create_new_repo(message):
    if message.content.split()[2] in next(os.walk("DisGit_Repos"))[1]:
        await message.channel.send("Repo Name already taken.")
        return
    else:
        os.mkdir(f"DisGit_Repos/{message.content.split()[2]}")
        os.mkdir(f"DisGit_Repos/{message.content.split()[2]}/Files")
        with open(f"DisGit_Repos/{message.content.split()[2]}/README.md", "w") as f:
            f.write("This repo has no description yet")
        await message.channel.send("Repo successfully created")
        return


async def remove_repo(message):
    shutil.rmtree(f"DisGit_Repos/{message.content.split()[2]}")
    await message.channel.send("Repo removed")


def disgit_help_function():
    embed = discord.Embed(title="DisGit Help")
    embed.add_field(name= "git -h", value = "You got to this menu so you must know how to use it", inline=True)
    embed.add_field(name="git -new", value="Creates a new repository with the passed name", inline=True)
    embed.add_field(name="git -remove", value="Deletes the repository that is passed", inline=True)
    embed.add_field(name="git -list", value="Lists all repositories", inline=True)
    return embed


async def edit_repo_description(message):
    repos = next(os.walk("DisGit_Repos"))[1]
    if message.content.split()[3] not in repos:
        await message.channel.send("Repo not found")
        return
    new_descript_words = message.content.split()[4:]
    description = ""
    for word in new_descript_words:
        description += word + " "
    author = message.author
    new_description = f"{description} by -{author}"
    with open(f"DisGit_Repos/{message.content.split()[3]}/README.md", "w") as f:
        f.write(new_description)
    await message.channel.send("Description successfully updated")


def repo_list():
    embed = discord.Embed(title="Repository List")
    for folder in next(os.walk("DisGit_Repos"))[1]:
        with open(f"DisGit_Repos/{folder}/README.md", "r") as f:
            description = f.read()
        embed.add_field(name=folder, value=description)
    return embed

def repo_list_files(message):
    embed = discord.Embed(title="File List")
    folder = message.content.split()[3]
    fp = f"DisGit_Repos/{folder}/Files"
    for file in os.listdir(fp):
        embed.add_field(name=file, value="It's a file")
    return embed


# function that gets list of attachments as discord cdn links
async def add_file(message):
    global ACCEPTED_FORMATS
    channel = message.channel
    fp = f"DisGit_Repos/{message.content.split()[3]}/Files", "r"
    for attachment in message.attachments:
        attachment_name = attachment.filename
        if attachment_name.split(".")[1] in ACCEPTED_FORMATS:
            url = attachment.url
            attachment_fp = f"DisGit_Repos/{message.content.split()[3]}/Files/{attachment_name}"
            file_from_url(attachment_fp, url)
            await channel.send(f"File: {attachment_name}; Successfully saved")
        else:
            await channel.send(f"File: {attachment_name} is not one of the supported file types")


# function for editing repo properties
async def repo_edit(message):
    if message.content.split()[2] == "-d":
        await edit_repo_description(message)
        return
    elif message.content.split()[2] == "-p":
        await  add_file(message)
        return
    elif message.content.split()[2] == "-list":
        await  message.channel.send(embed=repo_list_files(message))
        return

# Function that processes messages
async def disgit_message_handler(message, client):
    channel = message.channel
    if message.author == client.user:
        return

    elif message.content.split()[0] == "git":
        if len(message.content.split()) == 1:
            await channel.send("Run git -h to access the help menu if you don't know what your doing")
            return
        elif message.content.split()[1] == "-h":
            await channel.send(embed=disgit_help_function())
            return
        elif message.content.split()[1] == "-new":
            await create_new_repo(message)
            return
        elif message.content.split()[1] == "-remove":
            await remove_repo(message)
            return
        elif message.content.split()[1] == "-list":
            await channel.send(embed=repo_list())
            return
        elif message.content.split()[1] == "-edit":
            await repo_edit(message)
            return

    else:
        return

