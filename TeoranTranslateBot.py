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
import TeoranTranslateData as Tdata

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

startTime = datetime.datetime.now() # start time

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
    await ctx.send(Tdata.helpmsg.format(p = prefix))

# translateDictReversed = {v:k for k,v in translateDict.items()} # reverses dict ex: 1:"a" becomes "a":1. Unused

# echoes translation from English to Teoran.
@bot.command()
async def translate(ctx, string):
# translateTable provided by TeoranTranslateData.py
    translateTable = str.maketrans(Tdata.translateDict)
    translatedString = string.translate(translateTable) # translate string using the dict

    # send the translated string and print to console
    await ctx.send(f"'{string}' translates to:")
    await ctx.send(translatedString)
    
    await botLog(f"Translating '{string}' To {translatedString}")

# echoes translation from English to Teoran ignoring caps and using easy to read letters.
@bot.command()
async def translateEasy(ctx, string):
    easyTable = str.maketrans(Tdata.easyDict)
    easyString = string.translate(easyTable)

    # translateTable provided by TeoranTranslateData.py
    translateTable = str.maketrans(Tdata.translateDict)
    translatedString = easyString.translate(translateTable) # translate string using the dict

    # send the translated string and print to console
    await ctx.send(f"'{easyString}' easy translates to:")
    await ctx.send(translatedString)
    
    await botLog(f"EasyTranslating '{string}' To {translatedString}")

# echoes translation from English to Teoran in emoji ids (for copying with nitro).
@bot.command()
async def translateRaw(ctx, string):
    # translateTable provided by TeoranTranslateData.py
    translateTable = str.maketrans(Tdata.translateDict)
    translatedString = string.translate(translateTable) # translate string using the dict

    # send the translated string and print to console
    await ctx.send(f"'{string}' raw translates to: (Copy and paste with nitro)")
    await ctx.send(f"`{translatedString}`")
    
    await botLog(f"Raw Translating '{string}' To {translatedString}")

# echoes uptime
@bot.command()
async def uptime(ctx):
    now = datetime.datetime.now()

    uptimeDelta = now - startTime
    uptimeDeltaFormatted = str(uptimeDelta).split(".")[0] # uptimeDelta to a string, split microseconds and only use HH:MM:SS

    startTimeFormatted = startTime.strftime("%d/%m/%y %H:%M:%S") # day/month/year hours:minutes:seconds

    uptimeMsg = f"""Start time: `{startTimeFormatted}`
Uptime: `{uptimeDeltaFormatted}`
    """
    
    await botLog("Uptime message recieved. " + uptimeMsg)
    await ctx.send(uptimeMsg)

bot.run(token)