import discord
from discord.ext import commands
import os, sys

class Admin():
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def self_bot(self, ctx):
		"""Reboots Jeeves into Self Bot mode"""
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
		if discord.utils.get(ctx.message.author.roles, name="Jeeves"):
			await self.bot.say("Goodbye.")
			await self.bot.logout()
		else:
			await self.bot.say("You do not have permission to use that command.")
			return

def setup(bot):
	bot.add_cog(Admin(bot))