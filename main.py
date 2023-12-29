import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
from src.commands.command1 import send_news_3H, latest_news 
#from bot_manager import botRun

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
#Bot = discord.Client(intents=intents)   # Connect the bot to discord server
Bot = commands.Bot(command_prefix='$HackerNews',intents=intents)
@Bot.event
async def on_ready():
    print("we have logged in as {0.user}".format(Bot))
    send_news_3H.start()
    



@Bot.event
async def on_message(message):
    if message.author == Bot.user:
        return
    if message.content.startswith("$News"):
        await message.channel.send("Hello there im here for youi have some News") 
    #if message.content.startswith("$HackerNews"):
        #latest_news(ctx)

#Bot.run(DISCORD_TOKEN)




