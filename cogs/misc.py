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

	@commands.command(pass_context=True)
	async def wink(self, ctx):
	    channel = self.bot.get_channel(ctx.message.channel.id)
	    await self.bot.send_file(channel, "images/wink.png")
	    await self.bot.delete_message(ctx.message)

def setup(bot):
	bot.add_cog(Misc(bot))