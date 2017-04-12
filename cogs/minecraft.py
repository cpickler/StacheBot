import discord
from discord.ext import commands
from mcstatus import MinecraftServer
import os

default_MC = os.environ["DEFAULT_MC"]


def setup(bot):
    bot.add_cog(Minecraft(bot))


class Minecraft:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def status(self):
        server = MinecraftServer.lookup(default_MC)
        embed = discord.Embed(title=default_MC)
        status = server.status()
        print(status.players.online)
        await self.bot.say(embed=embed)

