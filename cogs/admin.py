import discord
from discord.ext import commands
import os, sys
from cogs.log import *

class_name = 'admin'

class Admin():
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def self_bot(self, ctx):
		"""Reboots Jeeves into Self Bot mode"""
		command = sys._getframe().f_code.co_name
		log(class_name, command)
		if discord.utils.get(ctx.message.author.roles, name="Jeeves"):
			file = open("restart_status.txt", "w")
			file.write("1")
			file.close()
			await self.bot.say("Rebooting as self bot...")
			os.execl(sys.executable, sys.executable, *sys.argv)
		else:
			await self.bot.say("You do not have permission to use that command.")
			return
		

	@commands.command(pass_context=True)
	async def restart(self, ctx):
		"""Restarts Jeeves"""
		command = sys._getframe().f_code.co_name
		log(class_name, command)
		if discord.utils.get(ctx.message.author.roles, name="Jeeves"):
			file = open("restart_status.txt", "w")
			file.write("0")
			file.close()
			await self.bot.say("Rebooting...")
			os.execl(sys.executable, sys.executable, *sys.argv)
		else:
			await self.bot.say("You do not have permission to use that command.")
			return
		

	@commands.command(pass_context=True)
	async def logout(self, ctx):
		"""Shuts Jeeves Down"""
		command = sys._getframe().f_code.co_name
		log(class_name, command)
		if discord.utils.get(ctx.message.author.roles, name="Jeeves"):
			await self.bot.say("Goodbye.")
			await self.bot.logout()
		else:
			await self.bot.say("You do not have permission to use that command.")
			return


	@commands.command(pass_context=True)
	async def purge(self, ctx, amount=5):
		if discord.utils.get(ctx.message.author.roles, name="Jeeves"):
			amount = amount+1
			await self.bot.purge_from(ctx.message.channel, limit=int(amount))
		else:
			await self.bot.say("You do not have permission to use that command.")


	@commands.command(pass_context=True)
	async def mute(self, ctx, user_id=""):
		if discord.utils.get(ctx.message.author.roles, name="Jeeves"):
			file = open("kill.txt", "w")
			file.write(user_id)
			file.close()
			await self.bot.add_reaction(ctx.message, '\U0001F44C')
		else:
			await self.bot.say("You do not have permission to use that command.")
			return


	@commands.command(pass_context=True)
	async def unmute(self, ctx):
		if discord.utils.get(ctx.message.author.roles, name="Jeeves"):
			file = open("kill.txt", "w")
			file.close()
			await self.bot.add_reaction(ctx.message, '\U0001F44C')
		else:
			await self.bot.say("You do not have permission to use that command.")
			return
		

	
	async def on_message(self, message):
		file = open("kill.txt", "r")
		killed = file.read()
		if message.author.id == killed:
			await self.bot.delete_message(message)	

def setup(bot):
	bot.add_cog(Admin(bot))