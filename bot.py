import discord
import random
import requests
from discord.ext import commands

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

api_url = "https://public-api.tracker.gg/v2/apex/standard/profile/xbl/Peliman44"
my_headers = {'TRN-Api-Key' : '12afa2a2-5704-4963-ac86-48397db1501d', 'Accept' : 'application/json', 'Accept-Encoding' : 'gzip'}
params = {'legend'}

# message that chooses a random gametype
@discord_bot.command(name='mystats')
async def msg(ctx):
    stats = requests.get('https://public-api.tracker.gg/apex/v1/standard/profile/5/OhParfait', headers=my_headers, params = params)
    response = stats
    await ctx.send(response)
    

discord_bot.run(TOKEN)