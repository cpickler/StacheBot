import os

from discord.ext import commands

description = """StacheBot"""

extensions = [
    'cogs.wolfram',
    'cogs.minecraft',
    'cogs.admin'
]

bot = commands.Bot(command_prefix=commands.when_mentioned_or(), description=description)


@bot.event
async def on_ready():
    print('Logged in as:')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('------')


@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.event
async def on_voice_state_update(before, after):
    if after.voice.self_deaf is True:
        afk = after.server.afk_channel
        try:
            await bot.move_member(after, afk)
        finally:
            pass

if __name__ == '__main__':
    token = os.environ['DISCORD_TOKEN']
    wolfram_token = os.environ['WOLFRAM_APPID']

    for extension in extensions:
        bot.load_extension(extension)

    bot.run(token)





