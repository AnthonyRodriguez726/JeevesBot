import discord
from discord.ext import commands
import json

class Calendar():
	def __init__(self, bot):
		self.bot = bot



	@commands.command(pass_context=True)
	async def add_event(self, ctx, *, event):
		user = ctx.message.author.name
		await self.bot.say("What day is this event scheduled for?")
		day = await self.bot.wait_for_message(author=ctx.message.author)
		day = day.content
		await self.bot.say("Your event, "+event+", has been added to your calendar on "+day+" :calendar_spiral:")
		data = {}
		data[day] = event
		event_json = json.dumps(data)
		
		file = open('calendar/anthony.json')
		file.write(event_json)
		file.close()
		

def setup(bot):
	bot.add_cog(Calendar(bot))