import discord
from discord.ext import commands
import os, sys

class User_Based():
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def afk(self, ctx):
		"""Adds you to the afk list"""
		# 1 == afk | 0 == not afk
		initial_author = ctx.message.author.name
		initial_path = "afk/"+initial_author+".txt"
		check_path = os.path.exists(initial_path)
		if check_path == False:
			file = open(initial_path, "w+")
			file.write("0")
			file.close()

		initial_file = open(initial_path, 'r')
		initial_status = initial_file.readline()
		
		if initial_status == "1":
			await self.bot.delete_message(ctx.message)
		elif initial_status == "0":
			await self.bot.delete_message(ctx.message)
			author =  ctx.message.author.name
			path = "afk/"+author+".txt"
			file = open(path, 'w')
			file.write("1")
			file.close()
			await self.bot.say("*"+author+" is now AFK.*")
		else:
			await self.bot.delete_message(ctx.message)
			author =  ctx.message.author.name
			path = "afk/"+author+".txt"
			file = open(path, 'w')
			file.write("1")
			file.close()
			await self.bot.say("*"+author+" is now AFK.*")
		

	@commands.command(pass_context=True)
	async def back(self, ctx):
		"""Takes you off the afk list"""
		initial_author = ctx.message.author.name
		initial_path = "afk/"+initial_author+".txt"
		initial_file = open(initial_path, 'r')
		initial_status = initial_file.readline()

		if initial_status == "1":
			await self.bot.delete_message(ctx.message)
			author = ctx.message.author.name
			path = "afk/"+author+".txt"
			file = open(path, 'w')
			file.write("0")
			file.close()
			await self.bot.say("*"+author+" is no longer AFK.*")
		elif initial_status == "0":
			await self.bot.delete_message(ctx.message)
		else:
			await self.bot.delete_message(ctx.message)


def setup(bot):
	bot.add_cog(User_Based(bot))