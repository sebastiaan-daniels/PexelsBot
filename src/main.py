# Import statements and initialisations
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# Initialisations
load_dotenv()
bot = discord.Bot(debug_guilds=[os.getenv('GUILD_ID')]) #! Remove debug_guilds when in production

cogs_list = [
    None
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')


# General commands
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.event
async def on_slash_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.respond("This command does not exist.")
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.respond("This command seems to be incomplete.")
    if isinstance(error, commands.errors.CommandOnCooldown):
        await ctx.respond(error, ephemeral=True)
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.respond("You haven't got enough permissions to run this command.")


# Bot run command with token
bot.run(os.getenv('TOKEN'))  # run the bot with the token