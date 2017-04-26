import discord
from discord.ext import commands
import requests
from random import randint
import giphypop
import urllib.request
import sys
import glob, os
from cogs.log import *
import ntpath

g = giphypop.Giphy()

class_name = 'misc'

class Misc():
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True, hidden=True)
	async def test(self, ctx):
		command = sys._getframe().f_code.co_name
		log(class_name, command)

	@commands.command(pass_context=True)
	async def wink(self, ctx):
		""";)"""
		command = sys._getframe().f_code.co_name
		channel = self.bot.get_channel(ctx.message.channel.id)
		await self.bot.send_file(channel, "images/wink.png")
		await self.bot.delete_message(ctx.message)
		log(class_name, command)

	@commands.command()
	async def servers(self):
		"""Displays how many servers this bot is being used in"""
		command = sys._getframe().f_code.co_name
		servers = str(len(self.bot.servers))
		server_message = "Jeeves is currently being used on "+servers+" server(s)."
		await self.bot.say(server_message)
		log(class_name, command)

	@commands.command()
	async def how_to_beat_bowser(self):
		"""Gives the secret behind beating Bowser"""
		command = sys._getframe().f_code.co_name
		await self.bot.say("*SLAM HIS HEAD 3 TIMES*")
		log(class_name, command)

	@commands.command()
	async def urban(self, *, word):
		"""Searches Urban Dictionary"""
		command = sys._getframe().f_code.co_name
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
		"Example: \n%s \n\n\n"
		"Result %d of %d```"
		) % (word, definition, example, word_num+1, word_amount)

		await self.bot.say(urban_message)
		log(class_name, command)

	@commands.command(pass_context=True)
	async def xkcd(self, ctx):
		"""Displays a random xkcd comic"""
		command = sys._getframe().f_code.co_name
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
		log(class_name, command)

	@commands.command(pass_context=True)
	async def anime(self, ctx):
		command = sys._getframe().f_code.co_name
		image_path = "images/anime.png"
		await self.bot.send_file(ctx.message.channel, image_path)
		log(class_name, command)

	@commands.command()
	async def plug(self):
		command = sys._getframe().f_code.co_name
		"""Link to plug.dj room"""
		await self.bot.say("<https://plug.dj/e9d645de>")
		log(class_name, command)

	@commands.command()
	async def list(self):
		"""List of games"""
		command = sys._getframe().f_code.co_name
		await self.bot.say("Heroes of the Storm, League of Legends, Overwatch, Keep Talking and Nobody Explodes, Warcraft 3, Hearthstone, Starcraft 2, Tabletop Simulator, Dungeon Defenders, CS:GO, Town of Salem, Portal 2, Rock of Ages, Rocket League, GTA V")
		log(class_name, command)

	@commands.command()
	async def logs(self):
		command = sys._getframe().f_code.co_name
		file_paths = []
		commands = []
		usage = []
		command_log = {}
		for root, dirs, files in os.walk("command_log"):
			for file in files:
				if file.endswith(".txt"):
					log_path = os.path.join(root, file)
					file_name = ntpath.basename(log_path)
					file_paths.append(log_path)
					command_name = file_name.replace(".txt", "")
					commands.append(command_name)

		command_length = len(file_paths)
		for path in file_paths:
			file_object = open(path, "r")
			times_used = file_object.readline()
			usage.append(times_used)
		print(usage)
		counter = 0
		quick_counter = 0
		for time in usage:
			for time in usage:
				primary = usage[counter]
				compare = usage[quick_counter]
				if primary > compare:
					temp = usage[counter]
					usage[counter] = usage[quick_counter]
					usage[quick_counter] = temp
				quick_counter += 1
				if quick_counter >= len(usage):
					quick_counter = 0
			counter += 1
		print(usage)


	@commands.command(pass_context=True)
	async def poll(self, ctx, *, question):
		"""Creates a simple thumbs up/down poll"""
		await self.bot.delete_message(ctx.message)
		bot_message = await self.bot.say(question)
		await self.bot.add_reaction(bot_message, '\U0001F44D')
		await self.bot.add_reaction(bot_message, '\U0001F44E')








	async def on_message(self, message):
		custom = self.bot.get_all_emojis()
		if '420' in message.content:
			await self.bot.add_reaction(message, '\U0001F448')
			await self.bot.add_reaction(message, '\u0034\u20E3')
			await self.bot.add_reaction(message, '\u0032\u20E3')
			await self.bot.add_reaction(message, '\u0030\u20E3')
			await self.bot.add_reaction(message, '\U0001F449')
	
		if '4:20' in message.content:
			await self.bot.add_reaction(message, '\U0001F448')
			await self.bot.add_reaction(message, '\u0034\u20E3')
			await self.bot.add_reaction(message, '\u0032\u20E3')
			await self.bot.add_reaction(message, '\u0030\u20E3')
			await self.bot.add_reaction(message, '\U0001F449')

def setup(bot):
	bot.add_cog(Misc(bot))