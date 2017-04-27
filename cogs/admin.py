import json
from discord.ext import commands
import discord
import os
from pymongo import MongoClient

config_file = open('config.json', 'r+')

mongo = MongoClient(os.environ['MONGODB_URI'])
db = getattr(mongo, os.environ['MONGODB_NAME'])

config = json.load(config_file)


def valid_field(field):
    fields = ['mcservers']
    if field in fields:
        return True
    else:
        return False


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

    @config.command(enabled=False)
    @commands.has_permissions(administrator=True)
    async def set(self, option, value):
        if option in config.keys():
            pass

    @config.command(enabled=True, pass_context=True)
    @commands.has_permissions(administrator=True)
    async def add(self, ctx, field, option, value):
        server = ctx.message.server.id
        sub_field = '.'.join([field, option])
        if valid_field(field):
            getattr(db, server).update_one({"field": field}, {'$set': {sub_field: value}}, upsert=True)


