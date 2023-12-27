from discord.ext import commands, tasks
import requests
from utils import get_last_news, send_news

async def get_last_news():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(url)

    return 


async def send_news():
    return 


@commands.command()

async def latest_news ():
    return

@tasks.loop(hours = 3)

async def send_news_3H():
    return