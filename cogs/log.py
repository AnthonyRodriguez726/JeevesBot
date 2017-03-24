import discord
from discord.ext import commands
import sys

def log(class_name, command_name):
	path = "command_log/"+class_name+"/"+command_name+".txt"
	file = open(path, 'r')
	grab = file.readline()
	newNum = int(grab)+1
	newNum = str(newNum)
	file.close()

	file = open(path, 'w')
	file.write(newNum)
	file.close()
