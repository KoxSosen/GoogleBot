import discord
from discord.ext import commands
from googlesearch import search 

bot = commands.Bot(command_prefix = '', case_insensitive=True)
                  


@bot.event
async def on_ready():
    print("Bot fully loaded")
    await bot.change_presence(activity=discord.Game('Microsoft Excel 2009 Edition'))
            
    

@bot.command()
async def find(ctx,*, query):
    author = ctx.author.mention
    await ctx.channel.send(f"Here are the links related to your question {author} !") 
    async with ctx.typing(): 
        for j in search(query, tld="co.in", num=10, stop=10, pause=2):
            await ctx.send(f"\n:point_right: {j}") 
#async def g(ctx, arg):
     #   searchContent = ""
       # text = str(arg).split(' ')
     #   for i in range(2, len(text)):
          #  searchContent = searchContent + text[i]

       # for j in search(searchContent, tld="co.in", num=1, stop=1, pause=2):
         #   await ctx.send(j)
            
    
#@client.event
#async def on_message(message):
 #   if message.content.lower().startswith('google api'):
    #    content = message.content.lower()
       #      await message.channel.send('The Google Api is a feature rich, and amazing api to use for developers.')
                
@bot.event
async def on_message(message):
    content = message.content.lower()
    if "trash bot" in content or "bot trash" in content:
        await message.channel.send(f"No ur trash kid {message.author.mention}")      

bot.run("token")