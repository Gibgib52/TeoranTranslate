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
        - `{prefix}translateRaw "string"` : Translates a string into Teoran emoji ids (for copying with nitro)

<:Teoran_g:949162522173386752> Info:
    - Supports letters a-z, ? ; : # ! . and 0-9
    - only has lowercase Teoran

<:Teoran_g:949162522173386752> <:Teoran_i:949162522261454898> <:Teoran_t:949162521871413279> : `https://github.com/Gibgib52/TeoranTranslate`
    """

    await ctx.send(helpmsg)

translateDict = {
    # lowercase letters
    "a": "<:Teoran_a:949162522148216882> ",
    "b": "<:Teoran_b:949162522198556692> ",
    "c": "<:Teoran_c:949162522336956436> ",
    "d": "<:Teoran_d:949162521829441547> ",
    "e": "<:Teoran_e:949162522160791552> ",
    "f": "<:Teoran_f:949162522173374464> ",
    "g": "<:Teoran_g:949162522173386752> ",
    "h": "<:Teoran_h:949162522223730688> ",
    "i": "<:Teoran_i:949162522261454898> ",
    "j": "<:Teoran_j:949162522538303508> ",
    "k": "<:Teoran_k:949162522269851688> ",
    "l": "<:Teoran_l:949162522135629854> ",
    "m": "<:Teoran_m:949162522282430524> ",
    "n": "<:Teoran_n:949162522165002320> ",
    "o": "<:Teoran_o:949162522169184326> ",
    "p": "<:Teoran_p:949162522169212968> ",
    "q": "<:Teoran_q:949162522328576000> ",
    "r": "<:Teoran_r:949162522211127307> ",
    "s": "<:Teoran_s:949162522303426560> ",
    "t": "<:Teoran_t:949162521871413279> ",
    "u": "<:Teoran_u:949162522223722527> ",
    "v": "<:Teoran_v:949162522353762365> ",
    "w": "<:Teoran_w:949162522215321660> ",
    "x": "<:Teoran_x:949162521854607381> ",
    "y": "<:Teoran_y:949162522169192488> ",
    "z": "<:Teoran_z:949162521955299349> ",
    " ": "<:Teoran_space:949164879405780997> ",
    # numbers
    "1": "<:Teoran_1:949476249309425675> ",
    "2": "<:Teoran_2:949476249208774736> ",
    "3": "<:Teoran_3:949476248860643349> ",
    "4": "<:Teoran_4:949476249225531392> ",
    "5": "<:Teoran_5:949476249133256724> ",
    "6": "<:Teoran_6:949476249275879454> ",
    "7": "<:Teoran_7:949476249183612928> ",
    "8": "<:Teoran_8:949476248898379827> ",
    "9": "<:Teoran_9:949476248957095977> ",
    "0": "<:Teoran_0:949476249301024818> ",
    # punctuation and symbols
    "?": "<:Teoran_question:949476249070366761> ",
    ";": "<:Teoran_semicolon:949476249082937404> ",
    ":": "<:Teoran_colon:949476249095528480> ",
    "#": "<:Teoran_hash:949476248680284191> ",
    "!": "<:Teoran_exclamation:949476248831291423> ",
    ".": "<:Teoran_period:949476249166811216> ",
    "&": "<:Teoran_and:951664227557466194>",
    "@": "<:Teoran_at:951664227838484580>",
    "(": "<:Teoran_roundo:951664227586801765> ",
    ")": "<:Teoran_roundc:951664227855237160> ",
    "[": "<:Teoran_squareo:951664228018823208> ",
    "]": "<:Teoran_squarec:951664227951738910> ",
    "*": "<:Teoran_asterisk:951664227888795688> ",
    "=": "<:Teoran_equal:951664227574251602> ",
    "#": "<:Teoran_hash:951664227838468176> ",
    "{": "<:Teoran_curlyo:951664227863633970> ",
    "}": "<:Teoran_curlyc:951664227859443742> ",
    "+": "<:Teoran_plus:951664227892985856> ",
    "-": "<:Teoran_minus:951664227884609536> ",
}

# translateDictReversed = {v:k for k,v in translateDict.items()} # reverses dict ex: 1:"a" becomes "a":1. Unused

# echoes translation from English to Teoran.
@bot.command()
async def translate(ctx, string):
    
    preppedString = string.lower() # lower so capital letters dont suprise us
    translateTable = str.maketrans(translateDict)
    translatedString = preppedString.translate(translateTable) # translate string using the dict

    # send the translated string and print to console
    await ctx.send(f"'{string}' translates to:")
    await ctx.send(translatedString)
    
    await echoToOwner(f"Translating '{string}' To {translatedString}")

# echoes translation from English to Teoran in emoji ids.
@bot.command()
async def translateRaw(ctx, string):
    
    preppedString = string.lower() # lower so capital letters dont suprise us
    translateTable = str.maketrans(translateDict)
    translatedString = preppedString.translate(translateTable) # translate string using the dict

    # send the translated string and print to console
    await ctx.send(f"'{string}' raw translates to:")
    await ctx.send(f"`{translatedString}`")
    
    await echoToOwner(f"Raw Translating '{string}' To {translatedString}")

bot.run(token)