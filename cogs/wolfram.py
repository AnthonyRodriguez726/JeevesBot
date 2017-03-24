import discord
from discord.ext import commands
import urllib.request
from random import randint
from urllib.request import urlopen
import requests
from keys import wolfram_id
from cogs.log import *

class_name = 'wolfram'

class Wolfram():
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def simplewolf(self, *, search):
		"""Extremely Simple Wolfram Alpha Search"""
		command = sys._getframe().f_code.co_name
		search = search.replace(" ", "+")
		url = "http://api.wolframalpha.com/v1/result?appid="+wolfram_id+"&i="+search
		
		f = urlopen(url)
		answer = f.read()
		answer = answer.decode("utf-8")

		await self.bot.say(answer)
		log(class_name, command)

	@commands.command(pass_context=True)
	async def wolfram(self, ctx, *, search):
		"""A Bit Smarter Wolfram Alpha Search"""
		command = sys._getframe().f_code.co_name
		urlsearch = search.replace(" ", "+")
		url = "http://api.wolframalpha.com/v1/simple?appid=" + wolfram_id + "&i=" + urlsearch + ""
		image = search+".gif"
		number = randint(312,789239187)
		stringnumber = str(number)
		urllib.request.urlretrieve(url, "images/wolfram/"+stringnumber+".gif")
		image_path = "images/wolfram/"+stringnumber+".gif"
		resize = Image.open(image_path)
		resize.save(image_path, quality=50)

		await self.bot.send_file(ctx.message.channel, image_path, content=search)
		log(class_name, command)

def setup(bot):
	bot.add_cog(Wolfram(bot))

