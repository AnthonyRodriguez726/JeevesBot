from keys import *
import discord
import asyncio
import discord.utils
import datetime
import requests
import os, sys

from discord.ext import commands


cogs = ['cogs.edward', 'cogs.misc', 'cogs.user_based', 'cogs.apartment', 'cogs.recipe', 'cogs.admin', 'cogs.steam', 'cogs.google']

description = 'Jeeves Bot. Your personal helper bot.'

file_status = open("restart_status.txt", "r")
restart_status = file_status.readline()

if restart_status == "0":
    bot = commands.Bot(command_prefix='!', description=description)

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')
        channel = bot.get_channel('276237909378465794')
        errors = []
        for cog in cogs:
            try:
                bot.load_extension(cog)
            except (AttributeError, ImportError) as e:
                print("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
                errors.append("true")
            print("{} loaded.".format(cog))

        if "true" in errors:
            await bot.send_message(channel, 'Jeeves Online. Some Cogs Misfunctioned on Start-Up.')
        else:
            await bot.send_message(channel, 'Jeeves Online. All Cogs Loaded.')

elif restart_status == "1":
    bot = commands.Bot(command_prefix='!', self_bot=True)

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')
        channel = bot.get_channel('276237909378465794')
        errors = []
        for cog in cogs:
            try:
                bot.load_extension(cog)
            except (AttributeError, ImportError) as e:
                print("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
                errors.append("true")
            print("{} loaded.".format(cog))

        if "true" in errors:
            await bot.send_message(channel, 'Self Bot Online. Some Cogs Misfunctioned on Start-Up.')
        else:
            await bot.send_message(channel, 'Self Bot Online. All Cogs Loaded.')

else:
    bot = commands.Bot(command_prefix='!', description=description)

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')
        channel = bot.get_channel('276237909378465794')
        errors = []
        for cog in cogs:
            try:
                bot.load_extension(cog)
            except (AttributeError, ImportError) as e:
                print("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
                errors.append("true")
            print("{} loaded.".format(cog))

        if "true" in errors:
            await bot.send_message(channel, 'Jeeves Online. Some Cogs Misfunctioned on Start-Up.')
        else:
            await bot.send_message(channel, 'Jeeves Online. All Cogs Loaded.')



if restart_status == "0":
    bot.run(token)
elif restart_status == "1":
    bot.run(self_token, bot=False)
else:
    bot.run(token)

