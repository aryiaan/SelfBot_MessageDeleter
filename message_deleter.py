import discord
from discord import Client, Status
from discord.ext import commands
from colorama import Fore, Back, Style
from datetime import datetime
token ="put your token here"
prefix = "set the prefix of your bot "
client = commands.Bot(command_prefix=prefix, self_bot=True)
@client.event
async def on_ready():
    day = datetime.now() - client.user.created_at
    print(f"{Fore.GREEN}Logged in\nUser : {client.user}\nID : {client.user.id}\nCreation Date : {client.user.created_at} ({day.days})\nBadges : ")
    for badg in client.user.public_flags.all():
        if client.user.public_flags.all() == [ ]:
            print("Empty")
        else:
            print(badg)
    await client.change_presence(status=Status.invisible)
    
@client.command()
async def clear(ctx, limit=100):
    await ctx.message.delete()
    channel = await client.fetch_channel(ctx.channel.id)
    number = 0
    async for message in channel.history(): 
        if int(number) == int(limit):
            pass
        else:
                if message.author.id == client.user.id: 
                    await message.delete()
                    number += 1
                    print(f"{Fore.GREEN}{message.content} Deleted [{number}]{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Done[{number} messages Deleted]{Style.RESET_ALL}")
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        print(f"{Fore.RED}Pls provide a number to delete\nExample : {prefix}clear 100 {Style.RESET_ALL}")
client.run(token)