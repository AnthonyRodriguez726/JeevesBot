import discord
from discord.ext import commands
import requests
from keys import food_id, food_key
import urllib.request

class Recipe():
	def __init__(self, bot):
		self.bot = bot

	# --- RECIPES ---
	@commands.command(pass_context=True)
	async def recipe(self, ctx, *, ingredient):
	    url = "https://api.edamam.com/"
	    search = ingredient
	    search_addon = "search?q="+search
	    id_addon = "&app_id="+food_id
	    key_addon = "&app_key="+food_key
	    full_search = url+search_addon+id_addon+key_addon
	    channel = self.bot.get_channel(ctx.message.channel.id)
	    

	    r = requests.get(full_search)
	    recipe = r.json()
	    
	    url = recipe["hits"][0]["recipe"]["url"]
	    label = recipe["hits"][0]["recipe"]["label"]
	    image = recipe["hits"][0]["recipe"]["image"]
	    ingredients = recipe["hits"][0]["recipe"]["ingredientLines"]
	    calories = recipe["hits"][0]["recipe"]["calories"]
	    int(calories)

	    filename = image.split('/')[-1]
	    urllib.request.urlretrieve(image, "images/"+filename)
	    image_path = "images/"+filename

	    ingredient_list = []
	    for ing in ingredients:
	        ingredient_list.append(ing)

	    final_ingredients = ""
	    for ing in ingredient_list:
	        final_ingredients += ing+"\n"

	    recipe_message = (
	"**Here is the most relevant recipe based on your search.** \n \n"
	"%s\n"
	"Calories: %d \n \n"
	"URL to recipe: <%s> \n"
	    ) % (label, calories, url)

	    # await self.bot.say(recipe_message)
	    await self.bot.send_file(channel, image_path, content=recipe_message)

	@commands.command()
	async def get_recipes(self, *, ingredient, to_amount=5):
	    iteration = int(to_amount)

	    url = "https://api.edamam.com/"
	    search = ingredient
	    search_addon = "search?q="+search
	    id_addon = "&app_id="+food_id
	    key_addon = "&app_key="+food_key
	    from_addon = "&from=0"
	    to_addon = "&to="+str(to_amount)
	    full_search = url+search_addon+id_addon+key_addon+from_addon+to_addon

	    r = requests.get(full_search)
	    recipe = r.json()

	    url = recipe["hits"][1]["recipe"]["url"]
	    urls = []
	    counter = 0
	    for i in range(iteration):
	        urls.append(recipe["hits"][counter]["recipe"]["url"])
	        counter += 1

	    labels = []
	    labels_counter = 0
	    for i in range(iteration):
	        labels.append(recipe["hits"][labels_counter]["recipe"]["label"])
	        labels_counter += 1

	    recipe_counter = 0
	    recipes_message = "**Here are the most relevant recipes based on your search.**\n \n"
	    for i in range(iteration):
	        recipes_message += "%s \n<%s> \n \n" % (labels[recipe_counter], urls[recipe_counter])
	        recipe_counter += 1

	    await self.bot.say(recipes_message)

	@commands.command()
	async def ingredients(self, *, recipe):
	    url = "https://api.edamam.com/"
	    search = recipe
	    search_addon = "search?q="+search
	    id_addon = "&app_id="+food_id
	    key_addon = "&app_key="+food_key
	    full_search = url+search_addon+id_addon+key_addon

	    r = requests.get(full_search)
	    recipe = r.json()

	    url = recipe["hits"][1]["recipe"]["url"]
	    label = recipe["hits"][0]["recipe"]["label"]
	    ingredients = recipe["hits"][0]["recipe"]["ingredientLines"]

	    counter = 0
	    ingredients_message = "**%s**\n \n" % (label)
	    for i in range(len(ingredients)):
	        ingredients_message += recipe["hits"][0]["recipe"]["ingredientLines"][counter]+"\n"
	        counter += 1
	    ingredients_message += "\n<%s>" % (url)

	    await self.bot.say(ingredients_message)

def setup(bot):
	bot.add_cog(Recipe(bot))