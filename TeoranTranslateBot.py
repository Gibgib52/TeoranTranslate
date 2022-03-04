"""
    Translates english into "Teoran" from Gwain Saga through a discord bot.

    used https://www.youtube.com/watch?v=bq80J5rh4Cc as template
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
    latency = round(bot.latency * 1000)
    await ctx.send("Pong, {}ms".format(latency))
    print("ping recieved, latency: {}ms".format(latency))

bot.run(token)