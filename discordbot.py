
from discord_easy_commands import EasyBot
import pyjokes
import discord
import os
from dotenv import load_dotenv

joke = pyjokes.get_jokes(language='es', category='all')
intents = discord.Intents.all()
bot = EasyBot(intents = intents)

bot.setCommand('!youtube', 'www.youtube.com')
bot.setCommand('!instagram','syscursos')
bot.setCommand('!chiste', joke)

load_dotenv()

token = os.getenv("TOKEN")
bot.run(token)