import discord # importing the Discord library, use "pip install discord" or "conda install discord" to install it
from discord.ext import commands

intents = discord.Intents.default() # setting the intents the bot will be able to use, check it in the Discord Developers Portal so that the bot can send messages, etc.
intents.message_content = True # allowing the bot to send messages

bot = commands.Bot(
  intents=intents # assign intents to the bot
) # creating a bot instance, it is responsible for the application

@bot.event # decorator "@bot.event" allows you to listen for events
async def on_ready(): # we use an asynchronous "on_ready" function, it is executed when the bot is ready
   print("bot is ready") # sending a log, you can do anything else here, but if you want to do something related to the Discord API, use "await" before the command

bot.run("token") # replace the "token" with your token from the "Bot" tab in the Discord Developers Portal, and give it here (as a string), remember not to share it with ANYONE
