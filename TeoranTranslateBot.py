"""
    Translates english into "Teoran" from Gwain Saga through a discord bot.

    used https://www.youtube.com/watch?v=bq80J5rh4Cc as template

    uses Teoran Font v1.04 from https://fontstruct.com/fontstructions/show/1833685/teoran-font-v1-04 in the discord server for emojis
"""

from ast import Return
from ftplib import Error
from http.client import HTTPException
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

# echoes translation from English to Teoran.
@bot.command()
async def translate(ctx, string):
    await translate.normal(ctx, string)

# echoes translation from English to Teoran ignoring caps and using easy to read letters.
@bot.command()
async def translateEasy(ctx, string):
    await translate.easy(ctx, string)

# echoes translation from English to Teoran in emoji ids (for copying with nitro).
@bot.command()
async def translateRaw(ctx, string):
    await translate.raw(ctx, string)

# translates from teoran to english
@bot.command()
async def translateRev(ctx, string):
    await translate.reverse(ctx, string)

# echoes uptime
@bot.command()
async def uptime(ctx):
    now = datetime.datetime.now()
    nowFormatted = now.strftime("%d/%m/%y %H:%M:%S")

    uptimeDelta = now - startTime
    uptimeDeltaFormatted = str(uptimeDelta).split(".")[0] # uptimeDelta to a string, split microseconds and only use HH:MM:SS

    startTimeFormatted = startTime.strftime("%d/%m/%y %H:%M:%S") # day/month/year hours:minutes:seconds

    uptimeMsg = f"""Start time: `{startTimeFormatted}`
Now time: `{nowFormatted}`
Uptime: `{uptimeDeltaFormatted}`
    """
    
    await botLog("Uptime message recieved. " + uptimeMsg)
    await ctx.send(uptimeMsg)

# contains all the translation fucntions
class translate:
    # Check if translated string is > 2000 chars, if it is then message and return
    async def lenCheck(ctx, translatedString):
        if len(translatedString) > 2000:
            lenErrorString = f"Error: Translated string ({len(translatedString)}) is greater than 2000 chars. shorten your string."
            await ctx.send(lenErrorString)
            await botLog(lenErrorString)
            raise ValueError(lenErrorString)

    # echoes translation from English to Teoran.
    async def normal(ctx, string):
        # translateTable provided by TeoranTranslateData.py
        translateTable = str.maketrans(Tdata.translateDict)
        translatedString = string.translate(translateTable) # translate string using the dict

        # if msg too big raise error
        await translate.lenCheck(ctx, translatedString)

        # send the translated string and print to console
        await ctx.send(f"'{string}' translates to:")
        await ctx.send(translatedString)
        
        await botLog(f"Translating '{string}' To {translatedString}")

    # translates from teoran to english
    async def reverse(ctx, string):
        # translateTable provided by TeoranTranslateData.py
        translateTableRev = Tdata.translateRevDict
        splitList = string.split(" ") # split on space
        translatedString = ""

        # add space to end of each val in splitList
        splitList = [ "{} ".format(key) for key in splitList ]

        # translate splitList
        for val in splitList:
            if val in translateTableRev:
                translatedString += translateTableRev[val]

        # if msg too big raise error
        await translate.lenCheck(ctx, translatedString)

        # send the translated string and print to console
        await ctx.send(f"'{string}' reverse translates to:")
        await ctx.send(f"`{translatedString}`")
        
        await botLog(f"Reverse Translating '{string}' To {translatedString}")

    # echoes translation from English to Teoran in emoji ids (for copying with nitro).
    async def raw(ctx, string):
        # translateTable provided by TeoranTranslateData.py
        translateTable = str.maketrans(Tdata.translateDict)
        translatedString = string.translate(translateTable) # translate string using the dict

        # if msg too big raise error
        await translate.lenCheck(ctx, translatedString)

        # send the translated string and print to console
        await ctx.send(f"'{string}' raw translates to: (Copy and paste with nitro)")
        await ctx.send(f"`{translatedString}`")
        
        await botLog(f"Raw Translating '{string}' To {translatedString}")

    # echoes translation from English to Teoran ignoring caps and using easy to read letters.
    async def easy(ctx, string):
        easyTable = str.maketrans(Tdata.easyDict)
        easyString = string.translate(easyTable)

        # translateTable provided by TeoranTranslateData.py
        translateTable = str.maketrans(Tdata.translateDict)
        translatedString = easyString.translate(translateTable) # translate string using the dict

        # if msg too big raise error
        await translate.lenCheck(ctx, translatedString)

        # send the translated string and print to console
        await ctx.send(f"'{easyString}' easy translates to:")
        await ctx.send(translatedString)
        
        await botLog(f"EasyTranslating '{string}' To {translatedString}")

bot.run(token)