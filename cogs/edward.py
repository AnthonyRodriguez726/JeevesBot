import discord
from discord.ext import commands

class Edward():
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def edward(self):
		"""edward"""
		channel = self.bot.get_channel(ctx.message.channel.id)
		await self.bot.send_file(channel, "images/edward.png")
		await self.bot.delete_message(ctx.message)

	@commands.command(pass_context=True)
	async def edward_pls(self, ctx):
		"""edward..."""
		channel = self.bot.get_channel(ctx.message.channel.id)
		await self.bot.send_file(channel, "images/edward_pls.png")
		await self.bot.delete_message(ctx.message)

	@commands.command(pass_context=True)
	async def EDWARD(self, ctx):
		"""EDWARD"""
		channel = self.bot.get_channel(ctx.message.channel.id)
		await self.bot.send_file(channel, "images/EDWARD!.png")
		await self.bot.delete_message(ctx.message)

def setup(bot):
	bot.add_cog(Edward(bot))