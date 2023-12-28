from discord.ext import commands, tasks
from discord import Embed
import requests
import main
import json
from utils import get_last_news, send_news

async def get_latest_news():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(url)    
    storys_ids = response.json()[:5] 
    news = ""
    for story_id in storys_ids:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story_data = requests.get(story_url).json

    return {
        "title":"Breaking News",
        "description":"Something entersting happen",
        "image_url":"https://example.com/news_image.jpg",
        "url": "https://example.com/full_article",
    }



async def send_news():
    channelId = input("Give us the ChannelId where you want the bot to work: ")
    print("The bot {0.user}".format(main.Bot),f" will work on channelID {channelId}")
    # ChannelID for my server is: 1189989133674885322 
    channel = main.Bot.get_channel(channelId)
    
    # Fetch to the letest news
    latest_news = get_last_news() 

    # Creat rich embed for the news
    embed = Embed(
        title = latest_news["title"],
        description= latest_news["description"],
        url = latest_news["url"],
        color = 0x3498db
    )
    embed.set_thumbnail(url = latest_news["image_url"])

    message = await channel.send(embed=embed) # Post the News on the channel

    # Add imojis :
    await message.add_reaction('👍')
    await message.add_reaction('👎')
    

    return 


@commands.command()

async def latest_news ():
    return

@tasks.loop(hours = 3)

async def send_news_3H():
    return