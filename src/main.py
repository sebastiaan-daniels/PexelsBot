# Import statements and initialisations
import discord
from discord.ext import commands
from util import env_loader

# Initialisations
# ! Remove debug_guilds when in production
bot = discord.Bot(debug_guilds=[env_loader.EnvLoader().guild_id])

cogs_list = [
    'image',
    'misc',
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
bot.run(env_loader.EnvLoader().token)  # run the bot with the token
