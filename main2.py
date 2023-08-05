import os
import discord
from discord.ext import commands
import json
import requests
import sys
from random import choice as rchoice

bot = commands.Bot(command_prefix="?", self_bot=True)

endpoint_url = "https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags=%s&json=1&limit=1000&pid=%s"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
error_message = '<?xml version="1.0" encoding="UTF-8"?>'

tags_list = [
    "-loli",
    "-rape"
]

shadowBackup = {

}

# Create a string with all the tags with either "+" or "-" for rule34 api
def formatTags(tags):
    return "".join(f"+{i}" for i in tags)

def response_handler(response_item):
    # Check if the status code is not 200 (invalid)
    if response_item.status_code != 200:
        return False

    # Check if it has an error or not due to the lack of content
    if error_message in response_item.content.decode() or response_item.content.decode() == "":
        return False

    # Returns the formatted json content
    return json.loads(response_item.content.decode())


# Handles the request
def request_handler(tag, page):
    if (tag + str(page)) in shadowBackup.keys():
        return shadowBackup[tag + str(page)]

    # Formats the url so it works I guess
    formed_url = endpoint_url % (tag, page)

    # Makes a request to the endpoint url
    endpoint_request = requests.get(formed_url, headers=headers)

    # Returns the response from "response_handler()"
    response = response_handler(endpoint_request)

    shadowBackup[tag + str(page)] = response

    return response

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!!!")

@bot.command()
async def fcum(ctx):
    cTag = ["female_ejaculation"]
    if response := request_handler(formatTags([*tags_list, *cTag]), 1):
        while True:
            await ctx.send(rchoice(response)['file_url'])
    else:
        print("Error: Invalid response")

@bot.command()
async def ftouch(ctx):
    cTag = ["female_masturbation"]
    if response := request_handler(formatTags([*tags_list, *cTag]), 1):
        while True:
            await ctx.send(rchoice(response)['file_url'])
    else:
        print("Error: Invalid response")

@bot.command()
async def squirt(ctx):
    cTag = ["female_ejaculation"]
    if response := request_handler(formatTags([*tags_list, *cTag]), 1):
        while True:
            await ctx.send(rchoice(response)['file_url'])
    else:
        print("Error: Invalid response")

@bot.command()
async def titjob(ctx):
    cTag = ["titjob"]
    if response := request_handler(formatTags([*tags_list, *cTag]), 1):
        while True:
            await ctx.send(rchoice(response)['file_url'])
    else:
        print("Error: Invalid response")

@bot.command()
async def thighs(ctx):
    cTag = ["thick_thighs"]
    if response := request_handler(formatTags([*tags_list, *cTag]), 1):
        while True:
            await ctx.send(rchoice(response)['file_url'])
    else:
        print("Error: Invalid response")

@bot.command()
async def pussy(ctx):
    cTag = ["vagina"]
    if response := request_handler(formatTags([*tags_list, *cTag]), 1):
        while True:
            await ctx.send(rchoice(response)['file_url'])
    else:
        print("Error: Invalid response")

@bot.command()
async def hboobs(ctx):
    cTag = ["huge_breasts"]
    if response := request_handler(formatTags([*tags_list, *cTag]), 1):
        while True:
            await ctx.send(rchoice(response)['file_url'])
    else:
        print("Error: Invalid response")

@bot.command()
async def bass(ctx):
    cTag = ["big_ass"]
    if response := request_handler(formatTags([*tags_list, *cTag]), 1):
        while True:
            await ctx.send(rchoice(response)['file_url'])
    else:
        print("Error: Invalid response")

@bot.command()
async def ass(ctx):
    cTag = ["ass"]
    if response := request_handler(formatTags([*tags_list, *cTag]), 1):
        while True:
            await ctx.send(rchoice(response)['file_url'])
    else:
        print("Error: Invalid response")

@bot.command()
async def boobs(ctx):
    cTag = ["big_breasts"]
    if response := request_handler(formatTags([*tags_list, *cTag]), 1):
        while True:
            await ctx.send(rchoice(response)['file_url'])
    else:
        print("Error: Invalid response")

@bot.command()
async def female(ctx):
    cTag = ["female"]
    if response := request_handler(formatTags([*tags_list, *cTag]), 1):
        while True:
            await ctx.send(rchoice(response)['file_url'])
    else:
        print("Error: Invalid response")

@bot.command()
async def female2(ctx):
    cTag = ["female_only"]
    if response := request_handler(formatTags([*tags_list, *cTag]), 1):
        while True:
            await ctx.send(rchoice(response)['file_url'])
    else:
        print("Error: Invalid response")

def stop_bot():
  """Stops The Bot"""
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.command(description="stops the bot")
async def stop(ctx):
      await ctx.send("Stopping...")
      stop_bot()

TOKEN = "YOUR TOKEN HERE"

bot.run(TOKEN)
