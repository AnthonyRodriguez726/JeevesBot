from keys import *
import discord
import asyncio
from discord.ext import commands
import discord.utils
import time
import datetime
import requests
import urllib.request
from urllib.parse import urlparse
from os.path import splitext
import os, sys

import steamsearch
import forecastio


api_key = weather_key
lat = 28.602427
lng = -81.200060

forecast = forecastio.load_forecast(api_key, lat, lng)

steamsearch.set_key(steam_key, "anotherSession", cache=True)

description = 'Jeeves Bot. Your personal helper bot.'

bot = commands.Bot(command_prefix='!', description=description)



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def jeeves():
    await bot.say(
        """```Here's what I can do:
        ```
        """
    )

@bot.command()
async def hello(description="Says Hello!"):
    await bot.say("Hello!")

# --- SHOPPING LIST ---
@bot.command()
async def add_item(item):
    need_file = open("need_list.txt", "r")
    need_lines = need_file.readlines()
    need_file.close()

    listLen = len(need_lines)
    need_lines.insert(listLen, item+"\n")
    itemMessage = item + " has been added to your shopping list."
    await bot.say(itemMessage)

    lenList = len(need_lines)
    file = open("need_list.txt", "w")
    counter = 0
    for _ in range(lenList):
        line = need_lines[counter]
        file.write(line)
        counter += 1
    file.close()

@bot.command()
async def remove_item(item):
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

@bot.command()
async def need_list():
    need_list = "```Here is your current shopping list:\n\n"

    file = open("need_list.txt", "r")
    lines = file.readlines()

    counter = 0
    for _ in range(len(lines)):
        need_list+="%s\n" % (lines[counter])
        counter += 1
    need_list+="```"
    await bot.say(need_list)

# --- TO DO LIST ---
@bot.command()
async def add_task(item):
    need_file = open("to_do.txt", "r")
    need_lines = need_file.readlines()
    need_file.close()

    listLen = len(need_lines)
    need_lines.insert(listLen, item+"\n")
    itemMessage = item + " has been added to your to do list."
    await bot.say(itemMessage)

    lenList = len(need_lines)
    file = open("to_do.txt", "w")
    counter = 0
    for _ in range(lenList):
        line = need_lines[counter]
        file.write(line)
        counter += 1
    file.close()

@bot.command()
async def remove_task(item):
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
    await bot.say(task_message)

@bot.command()
async def to_do():
    to_do = "```Here is your current to do list:\n\n"

    file = open("to_do.txt", "r")
    lines = file.readlines()

    counter = 0
    for _ in range(len(lines)):
        to_do+="%s\n" % (lines[counter])
        counter += 1
    to_do+="```"
    await bot.say(to_do)

# --- RECIPES ---
@bot.command()
async def recipe(ingredient):
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

    await bot.say(recipe_message)

@bot.command()
async def get_recipes(ingredient, to_amount):
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
        print(urls)
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

    await bot.say(recipes_message)

@bot.command()
async def ingredients(recipe):
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

    await bot.say(ingredients_message)

@bot.command()
async def servers():
    servers = str(len(bot.servers))
    server_message = "Jeeves is currently being used on "+servers+" server(s)."
    await bot.say(server_message)

@bot.command()
async def how_to_beat_bowser():
    await bot.say("*SLAM HIS HEAD 3 TIMES*")


@bot.command()
async def restart():
    await bot.say("Restarting...")
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.command()
async def logout():
    await bot.say("Goodbye.")
    await bot.logout()

# -STEAM METHODS-
@bot.command()
async def steam_sales(limit=7):

    specials = steamsearch.specials(limit=limit)
    games = [special for special in specials]

    counter = 0
    titles = []
    for game in games:
        titles.append(game.title)
        counter += 1

    discountPrices = []
    for game in games:
        discountPrices.append(game.discountPrice)
        counter += 1

    discounts = []
    for game in games:
        discounts.append(game.discount)
        counter += 1

    prices = []
    for game in games:
        prices.append(game.price)
        counter += 1

    id_counter = 0
    game_ids = []
    for _ in range(limit):
        game_package = steamsearch.get_app(titles[id_counter])
        game_ids.append(game_package[0])
        id_counter += 1

    deal_counter = 0
    game_deals = "--- STEAM SALES ---\n\n"
    for _ in range(limit):
        game_deals+="Game Name: %s \nOriginal Price: %s \nDiscount: %s \nCurrent Price: %s \n<http://store.steampowered.com/app/%s/> \n\n" % (titles[deal_counter], prices[deal_counter], discounts[deal_counter], discountPrices[deal_counter], game_ids[deal_counter])
        deal_counter += 1

    
    await bot.say(game_deals)

@bot.command()
async def most_played(limit=5):
    most_played = steamsearch.top_game_playercounts(limit=limit)

    playercounts = "--- TOP PLAYERCOUNTS --- \n\n"
    counter = 0
    for _ in range(limit):
        playercounts+="Game Title: %s \nCurrent Players: %s \nPeak Players: %s \nURL: <%s> \n \n" % (most_played[counter][2], most_played[counter][0], most_played[counter][1], most_played[counter][3])
        counter += 1

    await bot.say(playercounts)

@bot.command()
async def top_sellers(limit=5):
    top_sellers = steamsearch.top_sellers(limit=limit)
    games = [top_seller for top_seller in top_sellers]

    counter = 0
    titles = []
    for game in games:
        titles.append(game.title)
        counter += 1

    id_counter = 0
    game_ids = []
    for _ in range(limit):
        game_package = steamsearch.get_app(titles[id_counter])
        game_ids.append(game_package[0])
        id_counter += 1

    deal_counter = 0
    top_games = "--- TOP SELLERS ---\n\n"
    for _ in range(limit):
        top_games+="%s - <http://store.steampowered.com/app/%s/> \n\n" % (titles[deal_counter], game_ids[deal_counter])
        deal_counter += 1

    await bot.say(top_games)

@bot.command()
async def new_releases(limit=5):
    new_releases = steamsearch.new_releases(limit=limit)
    games = [new_release for new_release in new_releases]

    counter = 0
    titles = []
    for game in games:
        titles.append(game.title)
        counter += 1

    id_counter = 0
    game_ids = []
    for _ in range(limit):
        game_package = steamsearch.get_app(titles[id_counter])
        game_ids.append(game_package[0])
        id_counter += 1

    release_counter = 0
    releases = "--- NEW RELEASES ---\n\n"
    for _ in range(limit):
        releases+="%s - <http://store.steampowered.com/app/%s/> \n\n" % (titles[release_counter], game_ids[release_counter])
        release_counter += 1

    await bot.say(releases)


async def my_background_task():
    await bot.wait_until_ready()
    counter = 0
    channel = discord.Object(id=280886485438169090)

    byDay = forecast.daily()

    weatherData = []
    for current in byDay.data:
        weatherData.append(current.summary)

    minTemp = []
    for current in byDay.data:
        minTemp.append(current.temperatureMin)

    maxTemp = []
    for current in byDay.data:
        maxTemp.append(current.temperatureMax)

    rainChance = []
    for current in byDay.data:
        rainChance.append(current.precipProbability)



    updateMsg = """```Here is your daily update.\n\n
-----Weather-----\n
%s\n
Min Temperature: %s\n
Max Temperature: %s\n
Rain Chance: %d\n\n

-----Shopping List-----\n
test

    ```
    """ % (weatherData[0], minTemp[0], maxTemp[0], rainChance[0])

    while not bot.is_closed:
        counter += 1
        await bot.send_message(channel, updateMsg)
        await asyncio.sleep(86400) # task runs every 60 seconds

bot.loop.create_task(my_background_task())

# - WEATHER METHODS -



@bot.command()
async def weekly_forecast():
    weatherMessage = ("```--- Here is your weekly weather forecast ---\n\n")
    byDay = forecast.daily()

    weatherData = []
    for dailyData in byDay.data:
        weatherData.append(dailyData.summary)

    minTempData = []
    for dailyData in byDay.data:
        minTempData.append(dailyData.temperatureMin)

    maxTempData = []
    for dailyData in byDay.data:
        maxTempData.append(dailyData.temperatureMax)

    rainChance = []
    for dailyData in byDay.data:
        conversion = dailyData.precipProbability * 100
        rainChance.append(conversion)

    options = {
            "Sunday":{
                0: "Today",
                1: "Monday",
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday",
                7: "Sunday"
            },
            "Monday":{
                0: "Today",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday",
                6: "Sunday",
                7: "Monday"
            },
            "Tuesday":{
                0: "Today",
                1: "Wednesday",
                2: "Thursday",
                3: "Friday",
                4: "Saturday",
                5: "Sunday",
                6: "Monday",
                7: "Tuesday"
            },
            "Wednesday":{
                0: "Today",
                1: "Thursday",
                2: "Friday",
                3: "Saturday",
                4: "Sunday",
                5: "Monday",
                6: "Tuesday",
                7: "Wednesday"
            },
            "Thursday":{
                0: "Today",
                1: "Friday",
                2: "Saturday",
                3: "Sunday",
                4: "Monday",
                5: "Tuesday",
                6: "Wednesday",
                7: "Thursday"
            },
            "Friday":{
                0: "Today",
                1: "Saturday",
                2: "Sunday",
                3: "Monday",
                4: "Tuesday",
                5: "Wednesday",
                6: "Thursday",
                7: "Friday"
            },
            "Saturday":{
                0: "Today",
                1: "Sunday",
                2: "Monday",
                3: "Tuesday",
                4: "Wednesday",
                5: "Thursday",
                6: "Friday",
                7: "Saturday"
            }
        }

    todaysDay = time.strftime("%A")
    counter = 0
    for _ in range(len(weatherData)):

        weatherMessage += "%s - %s\nTemperate Min: %d\nTemperate Max: %d\nRain Change: %d%%\n\n" % (options[todaysDay].get(counter), weatherData[counter], minTempData[counter], maxTempData[counter], rainChance[counter])
        counter += 1

    weatherMessage += "```" 

    await bot.say(weatherMessage)



bot.run(token)
