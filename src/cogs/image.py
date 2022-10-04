# Imports
import discord
from discord.ext import commands

# cog class


class Image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"{self.__class__.__name__} Cog has been loaded")

    # cog commands
    @discord.slash_command()
    async def image(self, ctx):
        await ctx.respond("This is an image command.")


def setup(bot):
    bot.add_cog(Image(bot))
