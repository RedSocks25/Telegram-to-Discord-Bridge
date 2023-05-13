from discord import Intents
from discord.ext import commands

from dotenv import load_dotenv
import os


load_dotenv()


bot = commands.Bot(command_prefix='!', intents=Intents.default())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")



@bot.command()
async def send_message(ctx):
    print('Try to send message')
    channel = bot.get_channel(int(os.getenv('DISCORD_CHANNEL')))
    await channel.send('como estas?')


if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_BOT_TOKEN'))