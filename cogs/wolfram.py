import discord
from discord.ext import commands
import urllib.request
from urllib.request import urlopen
import requests
from keys import wolfram_id

class Wolfram():
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def wolfram(self, *, search):
		search = search.replace(" ", "+")
		url = "http://api.wolframalpha.com/v1/result?appid="+wolfram_id+"&i="+search
		
		f = urlopen(url)
		answer = f.read()
		answer = answer.decode("utf-8")

		await self.bot.say(answer)

def setup(bot):
	bot.add_cog(Wolfram(bot))

