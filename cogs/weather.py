import discord
from discord.ext import commands
import time
from keys import weather_key

import forecastio

api_key = weather_key
lat = 28.602427
lng = -81.200060

forecast = forecastio.load_forecast(api_key, lat, lng)

class Weather():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def weekly_forecast(self):
        """Displays the weekly forecast"""
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

        await self.bot.say(weatherMessage)

    #Rogue Weather Method
    async def my_background_task(self):
        await self.bot.wait_until_ready()
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
            rainChance.append(current.precipProbability*100)

            updateMsg = """```Here is your daily update.\n\n
    -----Weather-----\n
    %s\n
    Min Temperature: %s\n
    Max Temperature: %s\n
    Rain Chance: %d%%\n\n

    -----Shopping List-----\n
    test

            ```
            """ % (weatherData[0], minTemp[0], maxTemp[0], rainChance[0])

        while not self.bot.is_closed:
            counter += 1
            await self.bot.send_message(channel, updateMsg)
            await asyncio.sleep(86400) # task runs once per day

        self.bot.loop.create_task(my_background_task())

def setup(bot):
    bot.add_cog(Weather(bot))