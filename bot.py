#Discord bot - Billy. 
#Written by Ishaan Bahl/Illusion
#Uses the python hikari module

#Discord bot - Billy. 
#Written by Ishaan Bahl/Illusion
#Uses the python hikari module

import hikari
import lightbulb
import random

from BotReplies import words
from BotReplies import pings

bot = lightbulb.BotApp(token='bot tokem here')

#Checking if bot is online
@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('bot is on')

#Checks if bot was pinged anywhere
@bot.listen()
async def pingbot(event: hikari.GuildMessageCreateEvent): 
    
    if event.is_bot or not event.content:
        return

    if event.content.__contains__(f'<@!{935722968393334784}>'):
        picked = random.choice(pings)
        await event.message.respond(f"{picked} If you need help type `/info`. ")

#Slash "/info" command response
@bot.command
@lightbulb.command('info', 'Info on the creator and the bot!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
     #Embed stuff
    info =(
        hikari.Embed(
            title="Important Information."
        )
    )
    info.add_field(name='Contact Me on Discord:', value='Illusion#6971', inline=False)
    info.add_field(name='My Youtube:', value='https://www.youtube.com/channel/UCv4T2VUBOVuqDXfQ_gkQ1JA', inline=False)
    info.add_field(name='Features (This bot is 100% Slash Command Run):', value=' • The all-knowing 8ball. `/8ball` \n • Create your own story! `/madlibs` \n • My thoughts on dank meme-🤢. `/dankmemer`', inline=False)
    info.description="Hey, Im Ishaan Bahl/Illusion and I created this bot! While this was meant to be more of a personal project, if enough people are intrested I will make it more accessible to the public."
    info.set_footer(text="My website for more information: https://illusionstudioss.github.io/IllusionWebsite/")
    await ctx.respond(info)

#Mad Libs Game
@bot.command
@lightbulb.option('word_animal', 'Type in an animal!', type=str)
@lightbulb.option('word_color', 'Type in a color!', type=str)
@lightbulb.option('word_name', 'Type in name!', type=str)
@lightbulb.command('madlibs', 'Play a short game of MadLibs!')
@lightbulb.implements(lightbulb.SlashCommand)
async def generator(ctx):
    await ctx.respond(f"Once upon a time there was a kid named **{ctx.options.word_name}**. They were a terrible kid, and no one liked them. However, they took it too far when they said that they hated the color **{ctx.options.word_color}**. Now their parents were very angry, and left them in a forest where they were eaten by a **{ctx.options.word_animal}**. The End :D")
    
#Dank member beef command
@bot.command
@lightbulb.command('dankmemer', 'Ah my good friend dank...')
@lightbulb.implements(lightbulb.SlashCommand)
async def displaybeef(ctx):
    #Embed stuff
    embed =(
        hikari.Embed(
            title="My thoughts on Dank Memer."
        )
    )
    embed.description="Whos that? 😹 👎"
    embed.set_footer(text="Literally anything > Dank Memer")
    await ctx.respond(embed)

#8ball - dank memer ripoff but better lol
@bot.command
@lightbulb.option('question', 'Type in whatever your question is!')
@lightbulb.command('8ball','You need a anwser for something??')
@lightbulb.implements(lightbulb.SlashCommand)
async def ball(ctx):
    reply_message = random.choice(words)
    title_value = ctx.options.question #This lets the embeds title become the question asked
    #Embed stuff
    reply =(
        hikari.Embed(
            title=f"{title_value}?"
        )
    )
    reply.description= f"🎱{reply_message}"
    await ctx.respond(reply)

bot.run()