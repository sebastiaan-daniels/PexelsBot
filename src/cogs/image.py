# Imports
import discord
from discord.ext import commands
from discord.commands import Option
from util import api



class Image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"{self.__class__.__name__} Cog has been loaded")

    @discord.slash_command()
    async def image(self, ctx):
        await ctx.respond("This is an image command.")

    @discord.slash_command()
    async def test(self, ctx, search: Option(str, "What to search for", required=True)):
        t = await ctx.respond("This is a test command.")
        img = await api.api().get(params=search)
        await t.edit_original_message(content=f"{img}")

def setup(bot):
    bot.add_cog(Image(bot))
