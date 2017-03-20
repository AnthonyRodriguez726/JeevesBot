import discord
from discord.ext import commands

class Apartment_Only():
	def __init__(self, bot):
		self.bot = bot

	# --- SHOPPING LIST ---
	@commands.command(hidden=True)
	async def add_item(self, item):
		"""Adds an item to the shopping list"""
		need_file = open("need_list.txt", "r")
		need_lines = need_file.readlines()
		need_file.close()

		listLen = len(need_lines)
		need_lines.insert(listLen, item+"\n")
		itemMessage = item + " has been added to your shopping list."
		await self.bot.say(itemMessage)

		lenList = len(need_lines)
		file = open("need_list.txt", "w")
		counter = 0
		for _ in range(lenList):
			line = need_lines[counter]
			file.write(line)
			counter += 1
		file.close()

	@commands.command(hidden=True)
	async def remove_item(self, item):
		"""Removes an item from the shopping list"""
		need_file = open("need_list.txt", "r")
		need_lines = need_file.readlines()
		need_file.close()

		if item in need_lines: need_lines.remove(item)
		
		file = open("need_list.txt", "r")
		lines = file.readlines()
		file.close()

		file = open("need_list.txt", "w")
		for line in lines:
			if line!=item+"\n":
				file.write(line)
		file.close()
		item_message = item + " has been removed from your shopping list."

	@commands.command(hidden=True)
	async def need_list(self):
		"""Displays the shopping list"""
		need_list = "```Here is your current shopping list:\n\n"

		file = open("need_list.txt", "r")
		lines = file.readlines()

		counter = 0
		for _ in range(len(lines)):
			need_list+="%s\n" % (lines[counter])
			counter += 1
		need_list+="```"
		await self.bot.say(need_list)

	# --- TO DO LIST ---
	@commands.command(hidden=True)
	async def add_task(self, item):
		"""Adds a task to the to do list"""
		need_file = open("to_do.txt", "r")
		need_lines = need_file.readlines()
		need_file.close()

		listLen = len(need_lines)
		need_lines.insert(listLen, item+"\n")
		itemMessage = item + " has been added to your to do list."
		await self.bot.say(itemMessage)

		lenList = len(need_lines)
		file = open("to_do.txt", "w")
		counter = 0
		for _ in range(lenList):
			line = need_lines[counter]
			file.write(line)
			counter += 1
		file.close()

	@commands.command(hidden=True)
	async def remove_task(self, item):
		"""Removes a task from the to do list"""
		need_file = open("to_do.txt", "r")
		need_lines = need_file.readlines()
		need_file.close()

		if item in need_lines: need_lines.remove(item)
		
		file = open("to_do.txt", "r")
		lines = file.readlines()
		file.close()

		file = open("to_do.txt", "w")
		for line in lines:
			if line!=item+"\n":
				file.write(line)
		file.close()
		task_message = item + " has been removed from the to do list."
		await self.bot.say(task_message)

	@commands.command(hidden=True)
	async def to_do(self):
		"""Displays the to do list"""
		to_do = "```Here is your current to do list:\n\n"

		file = open("to_do.txt", "r")
		lines = file.readlines()

		counter = 0
		for _ in range(len(lines)):
			to_do+="%s\n" % (lines[counter])
			counter += 1
		to_do+="```"
		await self.bot.say(to_do)

def setup(bot):
	bot.add_cog(Apartment_Only(bot))