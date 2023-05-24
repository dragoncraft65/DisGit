# functions that work with the git style implementation

# imports
import os
import discord


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
        with open(f"DisGit_Repos/{message.content.split()[2]}/description.txt", "w") as f:
            f.write("This repo has no description yet")
        await message.channel.send("Repo successfully created")
        return


async def remove_repo(message):
    os.rmdir(f"DisGit_Repos/{message.content.split()[2]}")
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
    if message.content.split()[2] not in repos:
        await message.channel.send("Repo not found")
        return
    description = message.content.split()[2:]
    author = message.author
    new_description = f"{description} by -{author}"
    with open(f"DisGit_Repos/{message.content.split()[2]}/description.txt", "w") as f:
        f.write(new_description)
    await message.channel.send("Description successfully updated")


def repo_list():
    embed = discord.Embed(title="Repository LIst")
    for folder in next(os.walk("DisGit_Repos"))[1]:
        with open(f"DisGit_Repos/{folder}/description.txt", "r") as f:
            description = f.read()
        embed.add_field(name=folder, value=description)
    return embed


async def repo_edit(messsage):
    if messsage.content.split()[2] == "-d":
        await edit_repo_description(messsage)
        return


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

