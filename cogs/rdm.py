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
        Roll some dice combination, maximum sides and die are 100.
        :param die: [# of die]d[# of sides per die]
        :return: result of rolls
        """
        # Get necessary values from command
        m = re.match("^(?P<die>\d*)[dD](?P<sides>\d+)$", roll_expression)
        try:
            if m.group('die') == '':
                die = 1
            else:
                die = int(m.group('die'))
            sides = int(m.group('sides'))
        except AttributeError:
            await self.bot.say("Invalid roll expression, please use the form `[die]D[sides]` .")
            return

        # Verify an acceptable amount of dies and sides
        if die <= 100 and sides <= 100:
            # Roll the dice
            rolls = [random.randint(1, sides) for dice in range(die)]
            total = sum(rolls)

            # Print out the result
            roll_str = '` + `'.join(map(str, rolls))
            result_str = '**{total}** = `{rolls}`'.format(total=total, rolls=roll_str)
            await self.bot.say(result_str)
        else:
            # Return an error about the limits
            await self.bot.say("Oops! A maximum of 100 die with up to 100 sides each can be rolled per command.")

    @commands.command(aliases=['flip', 'coin', 'coinflip'])
    async def coinFlip(self):
        flip = random.getrandbits(1)
        if flip is True:
            result = 'Heads'
        else:
            result = 'Tails'

        await self.bot.say('You flipped **{}**.'.format(result))