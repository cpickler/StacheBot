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
        embed = discord.Embed(title=default_MC)
        server = MinecraftServer.lookup(default_MC)
        status = server.status()

        # Add Green color for a server that's up
        embed.colour = discord.Colour.green()

        # Add a list of online players
        if len(status.players.sample) >= 1:
            online_players = ''
            first = True
            for player in status.players.sample:
                if first is False:
                    online_players += '\n'
                online_players += player.name
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
        await self.bot.say(embed=embed)

