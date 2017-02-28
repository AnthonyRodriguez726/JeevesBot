import discord
from discord.ext import commands
import requests
from random import randint
import urllib.request

class Misc():
	def __init__(self, bot):
		self.bot = bot

	# @commands.command()
	# async def scissors(self):
	# 	"""You know how it is"""
	# 	await self.bot.say("**he was still hanging on... scissoring his legs uselessly...**")

	@commands.command(pass_context=True, hidden=True)
	async def test(self, ctx):
		"""Used for testing purposes"""
		print("test")

	@commands.command(pass_context=True)
	async def wink(self, ctx):
		""";)"""
		channel = self.bot.get_channel(ctx.message.channel.id)
		await self.bot.send_file(channel, "images/wink.png")
		await self.bot.delete_message(ctx.message)

	@commands.command()
	async def servers(self):
		"""Displays how many servers this bot is being used in"""
		servers = str(len(self.bot.servers))
		server_message = "Jeeves is currently being used on "+servers+" server(s)."
		await self.bot.say(server_message)

	@commands.command()
	async def how_to_beat_bowser(self):
		"""Gives the secret behind beating Bowser"""
		await self.bot.say("*SLAM HIS HEAD 3 TIMES*")

	@commands.command()
	async def urban(self, *, word):
		"""Searches Urban Dictionary"""
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
				word_num = 1
				search = url+word

		else:
			word = word.replace(" ", "+")
			search = url+word
			word_num = 1

		r = requests.get(search)
		definitions = r.json()
		word_num = int(word_num)
		word_num -= 1
		word_amount = len(definitions["list"])

		try:
			test = definitions["list"][word_num]["word"]
		except:
			await self.bot.say("There were no words matching your search.")
			return

		word = definitions["list"][word_num]["word"]
		definition = definitions["list"][word_num]["definition"]
		example = definitions["list"][word_num]["example"]
		
		urban_message = ("```Word: %s \n\n"
		"Definition: %s \n\n"
		"Example: %s \n\n\n"
		"Result %d of %d```"
		) % (word, definition, example, word_num+1, word_amount)

		await self.bot.say(urban_message)

	@commands.command(pass_context=True)
	async def xkcd(self, ctx):
		"""Displays a random xkcd comic"""
		url = "https://www.xkcd.com/"
		url_ext = "info.0.json"
		current_comic = url+url_ext

		r = requests.get(current_comic)
		current_json = r.json()
		current_num = current_json["num"]
		random_comic = str(randint(1,1803))
		random_url = url+"/"+random_comic+"/"+url_ext
		c = requests.get(random_url)
		comic = c.json()

		title = "**"+comic["safe_title"]+"**"
		image = comic["img"] 
		
		filename = image.split('/')[-1]
		urllib.request.urlretrieve(image, "images/xkcd/"+filename)
		image_path = "images/xkcd/"+filename

		await self.bot.send_file(ctx.message.channel, image_path, content=title)

	@commands.command(pass_context=True)
	async def anime(self, ctx):
		image_path = "images/anime.png"
		await self.bot.send_file(ctx.message.channel, image_path)


def setup(bot):
	bot.add_cog(Misc(bot))