import discord
from discord.ext import commands
import steamsearch
from keys import steam_key

steamsearch.set_key(steam_key, "anotherSession", cache=True)

class Steam():
    def __init__(self, bot):
        self.bot = bot

    # -STEAM METHODS-
    @commands.command()
    async def steam_sales(self, limit=7):

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

        
        await self.bot.say(game_deals)

    @commands.command()
    async def most_played(self, limit=5):
        most_played = steamsearch.top_game_playercounts(limit=limit)

        playercounts = "--- TOP PLAYERCOUNTS --- \n\n"
        counter = 0
        for _ in range(limit):
            playercounts+="Game Title: %s \nCurrent Players: %s \nPeak Players: %s \nURL: <%s> \n \n" % (most_played[counter][2], most_played[counter][0], most_played[counter][1], most_played[counter][3])
            counter += 1

        await self.bot.say(playercounts)

    @commands.command()
    async def top_sellers(self, limit=5):
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

        await self.bot.say(top_games)

    @commands.command()
    async def new_releases(self, limit=5):
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

        await self.bot.say(releases)

def setup(bot):
    bot.add_cog(Steam(bot))