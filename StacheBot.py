import os

from discord.ext import commands

description = """StacheBot"""

extensions = [
    'cogs.wolfram'
]

bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Logged in as:')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('------')


@bot.event
async def on_message(message):
    await bot.process_commands(message)

if __name__ == '__main__':
    token = os.environ['DISCORD_TOKEN']
    wolfram_token = os.environ['WOLFRAM_TOKEN']

    for extension in extensions:
        bot.load_extension(extension)

    bot.run(token)
