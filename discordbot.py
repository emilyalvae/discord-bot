
from discord_easy_commands import EasyBot
import pyjokes
import discord



token =  "MTEyNjM3MzcwODI2NTY5NzM5MA.G52OYp.typWUfgUKAeqLrS0RfMss2_XGTFpwJwMtRJQdw"


joke = pyjokes.get_jokes(language='es', category='all')
intents = discord.Intents.all()
bot = EasyBot(intents = intents)


bot.setCommand('!youtube', 'www.youtube.com')
bot.setCommand('!instagram','syscursos')
bot.setCommand('!chiste', joke)

bot.run(token)