from keys import *
import discord
import asyncio
from discord.ext import commands
import discord.utils
import time
import datetime
import requests

import steamsearch
import forecastio


def recipe(ingredient):
    url = "https://api.edamam.com/"
    search = ingredient
    search_addon = "search?q="+search
    id_addon = "&app_id="+food_id
    key_addon = "&app_key="+food_key
    full_search = url+search_addon+id_addon+key_addon
    
    r = requests.get(full_search)
    recipe = r.json()
    
    url = recipe["hits"][0]["recipe"]["url"]
    label = recipe["hits"][0]["recipe"]["label"]
    image = recipe["hits"][0]["recipe"]["image"]
    ingredients = recipe["hits"][0]["recipe"]["ingredientLines"]

    ingredient_list = []
    for ing in ingredients:
    	ingredient_list.append(ing)

    final_ingredients = ""
    for ing in ingredient_list:
    	final_ingredients += ing+"\n"
    
    recipe_message = """
    **Here is the most relevant recipe based on your search.** \n \n
    %s \n \n
    <%s> \n
    %s
    """ % (label, url, image)