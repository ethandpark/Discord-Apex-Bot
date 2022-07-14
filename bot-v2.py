from unicodedata import name
import discord
import random
import requests
from discord.ext import commands

stats = requests.get('https://api.mozambiquehe.re/bridge?auth=7d926f882681a8c248bdf5dac195f6e7&player=OhParfait&platform=PC')
print(stats)

TOKEN = "OTk0NjMzMzA5NTA4MzQ1OTM3.G8HSBg.bQQ0S3BiwO2gFtytql7RtoFfBtGIXvodyhCdZo"  

discord_bot = commands.Bot(command_prefix='!')

 # notify in console that script is running
@discord_bot.event
async def on_ready():
    print(f'{discord_bot.user} Service running')

# message when invalid command is used
@discord_bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("yo idk what that means")

# message that chooses a random legend
@discord_bot.command(name='randomlegend')
async def msg(ctx):
    legends = [
                "Bloodhound",
                (
                    "Gibby"
                ),
                (
                    "Lifeline"
                ),
                (
                    "Pathy"
                ),
                (
                    "Wraith"
                ),
                (
                    "Bangalore"
                ),
                (
                    "Caustic"
                ),
                (
                    "Mirage"
                ),
                (
                    "Octane"
                ),
                (
                    "Wattson"
                ),
                (
                    "Crypto"
                ),
                (
                    "Rev"
                ),
                (
                    "Loba"
                ),
                (
                    "Rampart"
                ),
                (
                    "Horizon"
                ),
                (
                    "Fuse"
                ),
                (
                    "Valk"
                ),
                (
                    "Seer"
                ),
                (
                    "Ash"
                ),
                (
                    "Mad Maggie"
                ),
                (
                    "Newcastle"
                ),
            ]
    response = random.choice(legends)
    await ctx.send(response)

# message that chooses a random gametype
@discord_bot.command(name='gamemode')
async def msg(ctx):
    gametype = [
                "Battle royale",
                (
                    'Arenas'
                )
            ]
    response = random.choice(gametype)
    await ctx.send(response)

# message that chooses a random gametype
@discord_bot.command(name='helpme')
async def msg(ctx):
    help = [
                """
                List of available commands:
                !randomlegend - picks a random legend
                !gamemode - chooses between BR and Arenas
                """
                
            ]
    response = random.choice(help)
    await ctx.send(response)

api_url = "https://public-api.tracker.gg/v2/apex/standard/profile/origin/"
my_headers = {'Content-Type' : 'application/json', 'TRN-Api-Key' : '12afa2a2-5704-4963-ac86-48397db1501d'}

# get the player's name from the API and return it as a string with the command !player
@discord_bot.command(name='player')
async def msg(ctx, *, player):
    player_url = api_url + player
    player_response = requests.get(player_url, headers=my_headers)
    player_json = player_response.json()
    player_name = player_json['nickname']
    await ctx.send(player_name)



@discord_bot.command(name='stats')
async def msg(ctx, arg):
    stats = requests.get(f'{api_url}{arg}', headers = my_headers)
    await ctx.send(arg)



discord_bot.run(TOKEN)