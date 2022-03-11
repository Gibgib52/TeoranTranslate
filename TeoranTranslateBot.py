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

from TransTable import translateDict

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

bot = commands.Bot(command_prefix=prefix, help_command=None)

# prints, also sends dm if dmlogging is true
async def echoToOwner(string):
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
    await echoToOwner(f"Logged in as {bot}")
    await echoToOwner(f"Prefix is: {prefix}")
    
# echoes the latency
@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000,1) # return latency in ms, rounded to 1 decimal
    await ctx.send(f"Pong, {latency}ms")
    await echoToOwner(f"ping recieved, latency: {latency}ms")

# echoes anything you put in quotes
@bot.command()
async def echo(ctx, string):
    await ctx.send(f"Echo : {string}")
    await echoToOwner(f"Echoing {string}")

@bot.command()
async def help(ctx):
    helpmsg = f"""<:Teoran_c:949162522336956436> Commands:
        Dont forget quotes!
        - `{prefix}help` : Echoes help
        - `{prefix}echo "string"` : Echoes a string
        - `{prefix}ping` : Echoes latency
        - `{prefix}translate "string"` : Translates a string into Teoran
        - `{prefix}translateRaw "string"` : Translates a string into Teoran emoji ids (for copying, if you have nitro)

<:Teoran_g:949162522173386752> Info:
    - Supports letters a-z, symbols and 0-9
    - Contact me if you find a bug. `Gibgib52#6473`

<:Teoran_g:949162522173386752> <:Teoran_i:949162522261454898> <:Teoran_tc:951687057384824912> : `https://github.com/Gibgib52/TeoranTranslate`
    """

    await ctx.send(helpmsg)

# translateDictReversed = {v:k for k,v in translateDict.items()} # reverses dict ex: 1:"a" becomes "a":1. Unused

# echoes translation from English to Teoran.
@bot.command()
async def translate(ctx, string):
    
    translateTable = str.maketrans(translateDict)
    translatedString = string.translate(translateTable) # translate string using the dict

    # send the translated string and print to console
    await ctx.send(f"'{string}' translates to:")
    await ctx.send(translatedString)
    
    await echoToOwner(f"Translating '{string}' To {translatedString}")

# echoes translation from English to Teoran in emoji ids (for copying with nitro).
@bot.command()
async def translateRaw(ctx, string):
    
    translateTable = str.maketrans(translateDict)
    translatedString = string.translate(translateTable) # translate string using the dict

    # send the translated string and print to console
    await ctx.send(f"'{string}' raw translates to:")
    await ctx.send(f"`{translatedString}`")
    
    await echoToOwner(f"Raw Translating '{string}' To {translatedString}")

bot.run(token)