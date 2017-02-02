from discord.ext import commands
import discord
import asyncio
import datetime, re
import json, asyncio
import copy
import logging
import traceback
import sys
from collections import Counter

client = discord.Client()

description = """
Hello! I am a bot written by Danny to provide some nice utilities.
"""

prefix = ['!', '\N{HEAVY EXCLAMATION MARK SYMBOL}']
bot = commands.Bot(command_prefix=prefix, description=description, pm_help=None)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if '420' in message.content:
        await client.add_reaction(message, '\U0001F448')
        await client.add_reaction(message, '\u0034\u20E3')
        await client.add_reaction(message, '\u0032\u20E3')
        await client.add_reaction(message, '\u0030\u20E3')
        await client.add_reaction(message, '\U0001F449')

    if '4:20' in message.content:
        await client.add_reaction(message, '\U0001F448')
        await client.add_reaction(message, '\u0034\u20E3')
        await client.add_reaction(message, '\u0032\u20E3')
        await client.add_reaction(message, '\u0030\u20E3')
        await client.add_reaction(message, '\U0001F449')

client.run('Mjc1NDczMzUzODUzMjM5Mjk2.C3LkcQ.y_7C-m-72dIo7a2g6nAzRlcuWx8')