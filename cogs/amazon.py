import discord
from discord.ext import commands
from amazon.api import AmazonAPI
import urllib.request
from keys import amazon_access_key, amazon_secret_key, amazon_assoc_tag

amazon = AmazonAPI(amazon_access_key, amazon_secret_key, amazon_assoc_tag)

class Amazon():
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def amazon(self, ctx, *, product):
		"""Searches amazon and gets the top result. (Not very smart)"""
		products = amazon.search_n(1, Keywords=product, SearchIndex='All')
		channel = ctx.message.channel
		title = products[0].title
		url = products[0].offer_url
		image = products[0].large_image_url
		price = products[0].price_and_currency[0]
		url = url.replace("?tag=incen-20", " ")

		filename = image.split('/')[-1]
		urllib.request.urlretrieve(image, "images/amazon/"+filename)
		image_path = "images/amazon/"+filename

		amazon_message = ("**%s**\n\n"
			"Price: $%s \n\n"
			"URL: %s \n\n"
			) % (title, price, url)

		await self.bot.send_file(channel, image_path, content=amazon_message)

def setup(bot):
	bot.add_cog(Amazon(bot))
