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

		roles = ctx.message.author.roles
		

	@commands.command(pass_context=True)
	async def wink(self, ctx):
		channel = self.bot.get_channel(ctx.message.channel.id)
		await self.bot.send_file(channel, "images/wink.png")
		await self.bot.delete_message(ctx.message)

	@commands.command()
	async def servers(self):
	    servers = str(len(bot.servers))
	    server_message = "Jeeves is currently being used on "+servers+" server(s)."
	    await self.bot.say(server_message)

	@commands.command()
	async def how_to_beat_bowser(self):
	    await self.bot.say("*SLAM HIS HEAD 3 TIMES*")

def setup(bot):
	bot.add_cog(Misc(bot))