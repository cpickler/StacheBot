import discord
from discord.ext import commands
import os, aiohttp

def setup(bot):
    bot.add_cog(WolframAlpha(bot))

wolfram_AppID = os.environ['WOLFRAM_APPID']

class WolframAlpha:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['wa', 'wolframalpha', 'wolfram'])
    async def wolframAlpha(self, *, query:str):
        """
        Ask the Wolfram Alpha site anything.
        Uses the Short Answer API for the response.
        There is a monthly limit, please don't abuse this command.
        :param query: Your question, 'what time is it in London?' for example.
        :return: Short Answer
        """
        url = "https://api.wolframalpha.com/v1/result"
        payload = {'appid': wolfram_AppID, 'i': query}

        with aiohttp.ClientSession() as session:
            async with session.get(url, params=payload) as resp:
                print(resp.headers)
                await self.bot.say(await resp.text())