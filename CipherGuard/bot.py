import discord
from discord.ext import commands, tasks


from .commands import News 


intents = discord.Intents.default()
intents.message_content = True

class CipherBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        # add more init things here
        

    @commands.event()
    async def on_ready(self):
        cogs = [News] # define list of cogs to load
        for cog in cogs:
            await self.add_cog(cog(self))
            print('Cogs: Loaded {cog}')
        print("we have logged in as {0.user}".format(self))

        news = self.bot.get_cog('News')
        if news is not None:
            news.send_news_3H.start()
    
    @commands.event
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith("$News"):
            await message.channel.send("Hello there im here for youi have some News") 
        #if message.content.startswith("$HackerNews"):
            #latest_news(ctx)





