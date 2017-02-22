import discord
from discord.ext import commands

class Misc():
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def scissors(self):
	    await self.bot.say("**he was still hanging on... scissoring his legs uselessly...**")

	@commands.command(pass_context=True)
	async def test(self, ctx):
	    print("test")

def setup(bot):
	bot.add_cog(Misc(bot))