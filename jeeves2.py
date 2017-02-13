import discord
from discord.ext import commands
import discord.utils

import steamsearch


steamsearch.set_key("05EFF505B55CAE53BD7066997BD106EE", "anotherSession", cache=True)

description = 'Jeeves Bot. Your personal helper bot.'

bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


def is_owner_check(message):
    return message.author.id == '140722560223543296'


@bot.command()
async def hello():
    await bot.say("Hello!")

@bot.command()
async def addItem(item):
    if items == None or items == '' or items == []:
        items = []
    listLen = len(items)
    items.insert(listLen, item)
    await bot.say(items)

@bot.command()
async def how_to_beat_bowser():
    await bot.say("*SLAM HIS HEAD 3 TIMES*")


@bot.command()
async def logout():
    exit()


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


bot.run('Mjc1NDczMzUzODUzMjM5Mjk2.C3LkcQ.y_7C-m-72dIo7a2g6nAzRlcuWx8')
