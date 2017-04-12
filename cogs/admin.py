import json
from discord.ext import commands
import discord

config_file = open('config.json', 'r+')

config = json.load(config_file)


def setup(bot):
    bot.add_cog(Admin(bot))


class Admin:
    def __init__(self, bot):
        self.bot = bot

    @commands.bot.group(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def config(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid command passed. . .')

    @config.command(enabled=False)
    @commands.has_permissions(administrator=True)
    async def set(self, option, value):
        if option in config.keys():
            pass
