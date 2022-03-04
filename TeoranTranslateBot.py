"""
    Translates english into "Teoran" from Gwain Saga through a discord bot.

    used https://www.youtube.com/watch?v=bq80J5rh4Cc as template

    uses Teoran Font v1.04 from https://fontstruct.com/fontstructions/show/1833685/teoran-font-v1-04 in the discord server for emojis
"""

import discord
from discord.ext import commands

import json
import os

# token loading and config
if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": "", "Prefix": "$"}

    with open(os.getcwd() + "/config.json","w+") as f:
        json.dump(configTemplate, f)

token = configData["Token"]
prefix = configData["Prefix"]

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Logged in as {}".format(bot))

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000,1) # return latency in ms, rounded to 1 decimal
    await ctx.send("Pong, {}ms".format(latency))
    print("ping recieved, latency: {}ms".format(latency))

@bot.command()
async def echo(ctx, string):
    await ctx.send(string)
    print("Echoing {}".format(string))

@bot.command()
async def translate(ctx, string):
    translateDict = {
        "a": ":Teoran_a: ",
        "b": ":Teoran_b: ",
        "c": ":Teoran_c: ",
        "d": ":Teoran_d: ",
        "e": ":Teoran_e: ",
        "f": ":Teoran_f: ",
        "g": "<:Teoran_g:949150356271673394> ",
        "h": ":Teoran_h: ",
        "i": ":Teoran_i: ",
        "j": ":Teoran_j: ",
        "k": ":Teoran_k: ",
        "l": ":Teoran_l: ",
        "m": ":Teoran_m: ",
        "n": ":Teoran_n: ",
        "o": ":Teoran_o: ",
        "p": ":Teoran_p: ",
        "q": ":Teoran_q: ",
        "r": ":Teoran_r: ",
        "s": ":Teoran_s: ",
        "t": ":Teoran_t: ",
        "u": ":Teoran_u: ",
        "v": ":Teoran_v: ",
        "w": ":Teoran_w: ",
        "x": ":Teoran_x: ",
        "y": ":Teoran_y: ",
        "z": ":Teoran_z: "
    }

    preppedString = string.lower() # lower so dict can translate
    translateTable = str.maketrans(translateDict)
    translatedString = preppedString.translate(translateTable) # translate string using the dict

    await ctx.send(translatedString)
    print("Translating {} To {}".format(string, translatedString))

bot.run(token)