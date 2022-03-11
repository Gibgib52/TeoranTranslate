"""
    Translates english into "Teoran" from Gwain Saga through a discord bot.

    used https://www.youtube.com/watch?v=bq80J5rh4Cc as template

    uses Teoran Font v1.04 from https://fontstruct.com/fontstructions/show/1833685/teoran-font-v1-04 in the discord server for emojis
"""

import discord
from discord.ext import commands

import json
import os
import datetime

# import translation tables, help message.
from TeoranTranslateData import *

# token loading and config
if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": "", "Prefix": "$", "OwnerID": "", "Dmlogging": "True"}

    with open(os.getcwd() + "/config.json","w+") as f:
        json.dump(configTemplate, f)

token = configData["Token"]
prefix = configData["Prefix"]
ownerId = configData["OwnerID"]
dmlogging = configData["DmLogging"]

# sets prefix and removes default help command
bot = commands.Bot(command_prefix=prefix, help_command=None)

# prints, also sends a dm if dmlogging is true
async def botLog(string):
    now = datetime.datetime.now()
    formattedTime = datetime.time(now.hour, now.minute, now.second)
    logstring = "[ {} ] OwnerLog: {}".format(formattedTime,string)
    if dmlogging == "True":
        owner = await bot.fetch_user(ownerId) # my discord user id
        await owner.send(logstring)
    print(logstring)

# logon message
@bot.event
async def on_ready():
    await botLog(f"Logged in as {bot}")
    await botLog(f"Prefix is: {prefix}")
    
# echoes the latency
@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000,1) # return latency in ms, rounded to 1 decimal
    await ctx.send(f"Pong, {latency}ms")
    await botLog(f"ping recieved, latency: {latency}ms")

# echoes anything you put in quotes
@bot.command()
async def echo(ctx, string):
    await ctx.send(f"Echo : {string}")
    await botLog(f"Echoing {string}")

@bot.command()
async def help(ctx):
    # helpmsg is in TeoranTranslateData.py
    await ctx.send(helpmsg.format(p = prefix))

# translateDictReversed = {v:k for k,v in translateDict.items()} # reverses dict ex: 1:"a" becomes "a":1. Unused

# echoes translation from English to Teoran.
@bot.command()
async def translate(ctx, string):
    # translateTable provided by TeoranTranslateData.py
    translateTable = str.maketrans(translateDict)
    translatedString = string.translate(translateTable) # translate string using the dict

    # send the translated string and print to console
    await ctx.send(f"'{string}' translates to:")
    await ctx.send(translatedString)
    
    await botLog(f"Translating '{string}' To {translatedString}")

# echoes translation from English to Teoran in emoji ids (for copying with nitro).
@bot.command()
async def translateRaw(ctx, string):
    # translateTable provided by TeoranTranslateData.py
    translateTable = str.maketrans(translateDict)
    translatedString = string.translate(translateTable) # translate string using the dict

    # send the translated string and print to console
    await ctx.send(f"'{string}' raw translates to:")
    await ctx.send(f"`{translatedString}`")
    
    await botLog(f"Raw Translating '{string}' To {translatedString}")

bot.run(token) # 100 lines :D