import discord
from discord.ext import commands
import random
import os
from cogs.log import *

class_name = 'edward'

class Edward():
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def edward(self, ctx):
		"""Displays a picture of Edward"""
		command = sys._getframe().f_code.co_name
		channel = self.bot.get_channel(ctx.message.channel.id)
		edwards = os.listdir('images/edward/')
		choice = random.choice(edwards)
		await self.bot.send_file(channel, "images/edward/"+choice)
		log(class_name, command)

	# @commands.command(pass_context=True)
	# async def edward_pls(self, ctx):
	# 	channel = self.bot.get_channel(ctx.message.channel.id)
	# 	await self.bot.send_file(channel, "images/edward_pls.png")

	# @commands.command(pass_context=True)
	# async def EDWARD(self, ctx):
	# 	channel = self.bot.get_channel(ctx.message.channel.id)
	# 	await self.bot.send_file(channel, "images/EDWARD!.png")
	# 	await self.bot.delete_message(ctx.message)

def setup(bot):
	bot.add_cog(Edward(bot))