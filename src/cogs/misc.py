# Imports
import discord
from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"{self.__class__.__name__} Cog has been loaded")

    # cog commands
    @discord.slash_command()
    async def ping(self, ctx):
        await ctx.respond(f"Bot latency: {round(self.bot.latency * 1000)}ms")


def setup(bot):
    bot.add_cog(Misc(bot))
