import discord
from discord.ext import commands
from mcstatus import MinecraftServer
import os
from pymongo import MongoClient

default_MC = os.environ["DEFAULT_MC"]

mongo = MongoClient(os.environ['MONGODB_URI'])
db = db = getattr(mongo, os.environ['MONGODB_NAME'])

def setup(bot):
    bot.add_cog(Minecraft(bot))


class Minecraft:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def status(self, ctx, mc_server="default"):
        server = ctx.message.server.id

        # Get the corresponding server address
        cursor = getattr(db, server).find_one()
        if cursor is None:
            mc_server = mc_server
        else:
            try:
                mc_server = cursor['mcservers'][mc_server]
            except KeyError:
                mc_server = mc_server

        embed = discord.Embed(title=mc_server)
        server = MinecraftServer.lookup(mc_server)
        status = server.status()

        # Add Green color for a server that's up
        embed.colour = discord.Colour.green()

        # Add a list of online players
        if status.players.sample is not None:
            online_players = ''
            first = True
            for player in status.players.sample:
                if first is False:
                    online_players += ', '
                name = ''
                for c in player.name:
                    if c == '_':
                        name += '\_'
                    else:
                        name += c
                online_players += name
                first = False
        else:
            online_players = 'No one is online!'

        embed.add_field(name="Players Online: {online}/{max}".format(online=status.players.online,
                                                                    max=status.players.max),
                        value=online_players)

        # Remove formatting codes from the description
        clean_description = ''
        del_char = False
        for i in status.description:
            if del_char is True:
                del_char = False
            elif i != '§':
                clean_description += i
            else:
                del_char = True

        embed.description = clean_description
        embed.set_footer(text="Ping: {ping} ms".format(ping=status.latency))
        await self.bot.say(embed=embed)

