import discord
from discord.ext import commands
import requests

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

	@commands.command()
	async def urban(self, *, word):
		"""Searches Urban Dictionary."""
		url = "http://api.urbandictionary.com/v0/define?term="

		if " " in word:
			split_word = word.rsplit(' ', 1)[0]
			word_num = word.rsplit(' ', 1)[1]

			has_digit = any(char.isdigit() for char in word_num)
			if has_digit:
				word = split_word
				int(word_num)

				word = word.replace(" ", "+")
				search = url+word
			else:
				word = word.replace(" ", "+")
				word_num = 0
				search = url+word

		else:
			word = word.replace(" ", "+")
			search = url+word
			word_num = 0

		r = requests.get(search)
		definitions = r.json()
		word_num = int(word_num)
		word = definitions["list"][word_num]["word"]
		definition = definitions["list"][word_num]["definition"]
		example = definitions["list"][word_num]["example"]
		
		urban_message = ("```Word: %s \n\n"
		"Definition: %s \n\n"
		"Example: %s \n```"
		) % (word, definition, example)

		await self.bot.say(urban_message)
		

		

		




def setup(bot):
	bot.add_cog(Misc(bot))