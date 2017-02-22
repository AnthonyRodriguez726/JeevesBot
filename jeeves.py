from keys import *
import discord
import asyncio
from discord.ext import commands
import discord.utils
import datetime
import requests
import urllib.request
from urllib.parse import urlparse
from os.path import splitext
from lxml import html
from lxml import etree
import os, sys
import aiohttp
from urllib.parse import parse_qs
import forecastio

import steamsearch

api_key = weather_key
lat = 28.602427
lng = -81.200060

forecast = forecastio.load_forecast(api_key, lat, lng)

steamsearch.set_key(steam_key, "anotherSession", cache=True)

cogs = ['cogs.edward', 'cogs.weather', 'cogs.misc']

description = 'Jeeves Bot. Your personal helper bot.'

file_status = open("restart_status.txt", "r")
restart_status = file_status.readline()

if restart_status == "0":
    bot = commands.Bot(command_prefix='!', description=description)

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')
        channel = bot.get_channel('276237909378465794')
        await bot.send_message(channel, 'Jeeves Online.')
        for cog in cogs:
            try:
                bot.load_extension(cog)
            except (AttributeError, ImportError) as e:
                print("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
                return
            print("{} loaded.".format(cog))

elif restart_status == "1":
    bot = commands.Bot(command_prefix='!', self_bot=True)

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')
        channel = bot.get_channel('276237909378465794')
        await bot.send_message(channel, 'Self Bot Online.')
        for cog in cogs:
            try:
                bot.load_extension(cog)
            except (AttributeError, ImportError) as e:
                print("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
        print("{} loaded.".format(cog))
else:
    bot = commands.Bot(command_prefix='!', description=description)

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')
        channel = bot.get_channel('276237909378465794')
        await bot.send_message(channel, 'Jeeves Online.')
        for cog in cogs:
            try:
                bot.load_extension(cog)
            except (AttributeError, ImportError) as e:
                print("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
                return
            print("{} loaded.".format(cog))

@bot.command(pass_context=True)
async def wink(ctx):
    channel = bot.get_channel(ctx.message.channel.id)
    await bot.send_file(channel, "images/wink.png")
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def afk(ctx):
    # 1 == afk | 0 == not afk
    initial_author = ctx.message.author.name
    initial_path = "afk/"+initial_author+".txt"
    check_path = os.path.exists(initial_path)
    if check_path == False:
        file = open(initial_path, "w+")
        file.write("0")
        file.close()

    initial_file = open(initial_path, 'r')
    initial_status = initial_file.readline()
    
    if initial_status == "1":
        await bot.delete_message(ctx.message)
    elif initial_status == "0":
        await bot.delete_message(ctx.message)
        author =  ctx.message.author.name
        path = "afk/"+author+".txt"
        file = open(path, 'w')
        file.write("1")
        file.close()
        await bot.say("*"+author+" is now AFK.*")
    else:
        await bot.delete_message(ctx.message)
        author =  ctx.message.author.name
        path = "afk/"+author+".txt"
        file = open(path, 'w')
        file.write("1")
        file.close()
        await bot.say("*"+author+" is now AFK.*")
    

@bot.command(pass_context=True)
async def back(ctx):
    initial_author = ctx.message.author.name
    initial_path = "afk/"+initial_author+".txt"
    initial_file = open(initial_path, 'r')
    initial_status = initial_file.readline()

    if initial_status == "1":
        await bot.delete_message(ctx.message)
        author = ctx.message.author.name
        path = "afk/"+author+".txt"
        file = open(path, 'w')
        file.write("0")
        file.close()
        await bot.say("*"+author+" is no longer AFK.*")
    elif initial_status == "0":
        await bot.delete_message(ctx.message)
    else:
        await bot.delete_message(ctx.message)



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
@bot.command(pass_context=True)
async def recipe(ctx, *, ingredient):
    url = "https://api.edamam.com/"
    search = ingredient
    search_addon = "search?q="+search
    id_addon = "&app_id="+food_id
    key_addon = "&app_key="+food_key
    full_search = url+search_addon+id_addon+key_addon
    channel = bot.get_channel(ctx.message.channel.id)
    

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

    recipe_message = """
**Here is the most relevant recipe based on your search.** \n
%s
Calories: %d \n
URL to recipe: <%s> \n
    """ % (label, calories, url)

    # await bot.say(recipe_message)
    await bot.send_file(channel, image_path, content=recipe_message)

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
async def ingredients(*,recipe):
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
async def self_bot():
    file = open("restart_status.txt", "w")
    file.write("1")
    file.close()
    await bot.say("Rebooting as self bot...")
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.command()
async def restart():
    file = open("restart_status.txt", "w")
    file.write("0")
    file.close()
    await bot.say("Rebooting...")
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




def parse_google_card(node):
    if node is None:
        return None

    e = discord.Embed(colour=0x738bd7)

    # check if it's a calculator card:
    calculator = node.find(".//table/tr/td/span[@class='nobr']/h2[@class='r']")
    if calculator is not None:
        e.title = 'Calculator'
        e.description = ''.join(calculator.itertext())
        return e

    parent = node.getparent()

    # check for unit conversion card
    unit = parent.find(".//ol//div[@class='_Tsb']")
    if unit is not None:
        e.title = 'Unit Conversion'
        e.description = ''.join(''.join(n.itertext()) for n in unit)
        return e

    # check for currency conversion card
    currency = parent.find(".//ol/table[@class='std _tLi']/tr/td/h2")
    if currency is not None:
        e.title = 'Currency Conversion'
        e.description = ''.join(currency.itertext())
        return e

    # check for release date card
    release = parent.find(".//div[@id='_vBb']")
    if release is not None:
        try:
            e.description = ''.join(release[0].itertext()).strip()
            e.title = ''.join(release[1].itertext()).strip()
            return e
        except:
            return None

    # check for definition card
    words = parent.find(".//ol/div[@class='g']/div/h3[@class='r']/div")
    if words is not None:
        try:
            definition_info = words.getparent().getparent()[1] # yikes
        except:
            pass
        else:
            try:
                # inside is a <div> with two <span>
                # the first is the actual word, the second is the pronunciation
                e.title = words[0].text
                e.description = words[1].text
            except:
                return None

            # inside the table there's the actual definitions
            # they're separated as noun/verb/adjective with a list
            # of definitions
            for row in definition_info:
                if len(row.attrib) != 0:
                    # definitions are empty <tr>
                    # if there is something in the <tr> then we're done
                    # with the definitions
                    break

                try:
                    data = row[0]
                    lexical_category = data[0].text
                    body = []
                    for index, definition in enumerate(data[1], 1):
                        body.append('%s. %s' % (index, definition.text))

                    e.add_field(name=lexical_category, value='\n'.join(body), inline=False)
                except:
                    continue

            return e

    # check for "time in" card
    time_in = parent.find(".//ol//div[@class='_Tsb _HOb _Qeb']")
    if time_in is not None:
        try:
            time_place = ''.join(time_in.find("span[@class='_HOb _Qeb']").itertext()).strip()
            the_time = ''.join(time_in.find("div[@class='_rkc _Peb']").itertext()).strip()
            the_date = ''.join(time_in.find("div[@class='_HOb _Qeb']").itertext()).strip()
        except:
            return None
        else:
            e.title = time_place
            e.description = '%s\n%s' % (the_time, the_date)
            return e

    # check for weather card
    # this one is the most complicated of the group lol
    # everything is under a <div class="e"> which has a
    # <h3>{{ weather for place }}</h3>
    # string, the rest is fucking table fuckery.
    weather = parent.find(".//ol//div[@class='e']")
    if weather is None:
        return None

    location = weather.find('h3')
    if location is None:
        return None

    e.title = ''.join(location.itertext())

    table = weather.find('table')
    if table is None:
        return None

    # This is gonna be a bit fucky.
    # So the part we care about is on the second data
    # column of the first tr
    try:
        tr = table[0]
        img = tr[0].find('img')
        category = img.get('alt')
        image = 'https:' + img.get('src')
        temperature = tr[1].xpath("./span[@class='wob_t']//text()")[0]
    except:
        return None # RIP
    else:
        e.set_thumbnail(url=image)
        e.description = '*%s*' % category
        e.add_field(name='Temperature', value=temperature)

    # On the 4th column it tells us our wind speeds
    try:
        wind = ''.join(table[3].itertext()).replace('Wind: ', '')
    except:
        return None
    else:
        e.add_field(name='Wind', value=wind)

    # On the 5th column it tells us our humidity
    try:
        humidity = ''.join(table[4][0].itertext()).replace('Humidity: ', '')
    except:
        return None
    else:
        e.add_field(name='Humidity', value=humidity)

    return e

async def get_google_entries(query):
    params = {
        'q': query,
        'safe': 'on'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)'
    }

    # list of URLs
    entries = []

    # the result of a google card, an embed
    card = None

    async with aiohttp.get('https://www.google.com/search', params=params, headers=headers) as resp:
        if resp.status != 200:
            raise RuntimeError('Google somehow failed to respond.')

        root = etree.fromstring(await resp.text(), etree.HTMLParser())

        # with open('google.html', 'w', encoding='utf-8') as f:
        #     f.write(etree.tostring(root, pretty_print=True).decode('utf-8'))

        """
        Tree looks like this.. sort of..
        <div class="g">
            ...
            <h3>
                <a href="/url?q=<url>" ...>title</a>
            </h3>
            ...
            <span class="st">
                <span class="f">date here</span>
                summary here, can contain <em>tag</em>
            </span>
        </div>
        """

        card_node = root.find(".//div[@id='topstuff']")
        card = parse_google_card(card_node)

        search_nodes = root.findall(".//div[@class='g']")
        for node in search_nodes:
            url_node = node.find('.//h3/a')
            if url_node is None:
                continue

            url = url_node.attrib['href']
            if not url.startswith('/url?'):
                continue

            url = parse_qs(url[5:])['q'][0] # get the URL from ?q query string

            # if I ever cared about the description, this is how
            entries.append(url)

            # short = node.find(".//span[@class='st']")
            # if short is None:
            #     entries.append((url, ''))
            # else:
            #     text = ''.join(short.itertext())
            #     entries.append((url, text.replace('...', '')))

    return card, entries

@bot.command(aliases=['google'])
async def g(*, query):
    """Searches google and gives you top result."""
    await bot.type()
    try:
        card, entries = await get_google_entries(query)
    except RuntimeError as e:
        await bot.say(str(e))
    else:
        if card:
            value = '\n'.join(entries[:3])
            if value:
                card.add_field(name='Search Results', value=value, inline=False)
            return await bot.say(embed=card)

        if len(entries) == 0:
            return await bot.say('No results found... sorry.')

        next_two = entries[1:3]
        if next_two:
            formatted = '\n'.join(map(lambda x: '<%s>' % x, next_two))
            msg = '{}\n\n**See also:**\n{}'.format(entries[0], formatted)
        else:
            msg = entries[0]

        await bot.say(msg)



#Rogue Weather Method
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
            await asyncio.sleep(86400) # task runs once per day

bot.loop.create_task(my_background_task())

if restart_status == "0":
    bot.run(token)
elif restart_status == "1":
    bot.run(self_token, bot=False)
else:
    bot.run(token)

