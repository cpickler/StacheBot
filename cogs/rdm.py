import discord
from discord.ext import commands
import random
import re

def setup(bot):
    bot.add_cog(RDM(bot))

class RDM:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, roll_expression):
        """
        Roll some dice combination
        :param die: [# of die]d[# of sides per die]
        :return: result of rolls
        """
        # TODO set limits to max # of dice and sides
        # Get necessary values from command
        m = re.match("^(?P<die>\d+)[dD](?P<sides>\d+)$", roll_expression)
        die = int(m.group('die'))
        sides = int(m.group('sides'))

        # Roll the dice
        rolls = [random.randint(1, sides) for dice in range[die]]
        total = sum(rolls)

        # Print out the result
        roll_str = ' + '.join(rolls)
        result_str = '**{total}** = {rolls}'.format(total=total, rolls=roll_str)
        await self.bot.say(result_str)