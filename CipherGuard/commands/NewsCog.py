import requests
import discord

from discord import Embed
from discord.ext import commands, tasks


class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def get_latest_news():
        url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        response = requests.get(url)    
        storys_ids = response.json()[:3]
        news = ""
        news_items =[] # make a list so we can store title and url of the news 
        for story_id in storys_ids:
            story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            story_data = requests.get(story_url).json()
            # ftech the news to the breaking news
            if story_data and "title" in story_data and "url" in story_data:
                news_item = {
                    "title": story_data["title"],
                    "image_url": story_data.get("image", ""),
                    "description": story_data.get("description", "No Description"),
                    "url": story_data["url"],
                }
                news_items.append(news_item)

        return news_items

    @commands.command()
    async def latest_news (self, ctx):
        latest_news = self.get_latest_news() 

        # Creat rich embed for the news
        for news_item in latest_news:
            embed = Embed(
            title = latest_news["title"],
            description= latest_news["description"],
            url = latest_news["url"],
            color = 0x3498db
            )
            embed.set_thumbnail(url = latest_news["image_url"])
            message = await ctx.send(embed=embed) # Post the News on the channel

            # Add emojis :
            await message.add_reaction('👍')
            await message.add_reaction('👎')

    async def send_news(self):
        await self.bot.wait_until_ready() # to fix Runtime error loop with main Bot.run
        channelId = int(input("Give us the ChannelId where you want the bot to work: "))
        print("The bot {0.user}".format(self),f" will work on channelID {channelId}")
        # ChannelID for my server is: 1189989133674885322 
        channelID = 1189989133674885322
        channel = self.bot.get_channel(channelID)
        # Fetch to the letest news
        latest_news = await self.get_latest_news() 

        # Creat rich embed for the news
        for news_item in latest_news:
            # fix url error 
            # fix the image url error
            title = news_item.get("title", "No title")
            description = news_item.get("description", "No description")
            url = news_item.get("url", "No url")
            image_url = news_item.get("image_url", "No image url")
            color = 0x3498db
            embed = Embed(
                title=title,
                description=description,
                color=color
            )

            if url.startswith(("http", "https")):
                embed.url = url

            if url and ("http://" in url or "https://" in url):
                embed.set_footer(text=url)
            else:
                pass
            print(f"Image URL: {image_url}") # to stacktrace and debug
            

            message = await channel.send(embed=embed) # Post the News on the channel

        # Add imojis :
            await message.add_reaction('👍')
            await message.add_reaction('👎')

    @tasks.loop(minutes = 5) # just test
    async def send_news_3H(self):
        await self.send_news()
    
    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.name}~')
        else:
            await ctx.send(f'Hello {member.name}... This feels familiar.')
        self._last_member = member

# Next plans :
    # improve get_latest_news() ,send_news() functions 
    # add a way to help user input his channel id on terminal then saving the channel id on json file to get access later when the bot reboots
    # impove commands 
    # add new ideas if possible 
    # fix the image errors, improve url embed
    