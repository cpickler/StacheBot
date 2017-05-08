import json
from discord.ext import commands
import discord
import os
from pymongo import MongoClient
import distutils.util as util

config_file = open('config.json', 'r+')

mongo = MongoClient(os.environ['MONGODB_URI'])
db = getattr(mongo, os.environ['MONGODB_NAME'])


def valid_option(option, return_option=False):
    options = ['mcservers', 'moveOnDeafen']
    if return_option is False:
        if option in options:
            return True
        else:
            return False
    elif return_option is True:
        option = str.lower(option)
        for valid in options:
            if option == valid.lower():
                return True, valid
        return False, None



def setup(bot):
    bot.add_cog(Admin(bot))


class Admin:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def config(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid command passed. . .')

    @config.command(enabled=True, pass_context=True)
    @commands.has_permissions(administrator=True)
    async def set(self, ctx, option, value):
        server = ctx.message.server.id

        # Convert value to proper type
        try:
            value = bool(util.strtobool(value))
        except ValueError:
            try:
                value = int(value)
            except ValueError:
                pass

        valid, option = valid_option(option, return_option=True)
        if valid:
            config_option = '.'.join(['config', option])
            getattr(db, server).update_one({"field": "config"}, {'$set': {config_option: value}}, upsert=True)

    @config.command(enabled=True, pass_context=True)
    @commands.has_permissions(administrator=True)
    async def add(self, ctx, option, field, value):
        option = str.lower(option)
        field = str.lower(field)
        server = ctx.message.server.id
        sub_field = '.'.join([option, field])
        if valid_option(option):
            getattr(db, server).update_one({"field": option}, {'$set': {sub_field: value}}, upsert=True)


