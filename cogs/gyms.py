import discord
from discord.ext import commands

class Regions:
    """Gym Leaders and More"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def trading(self,ctx):
        """Trading Info"""
        await self.bot.say("Hey " + ctx.message.author.mention + " you have been on the list for trading.")

    @commands.group(pass_context=True)
    async def regions(self,ctx):
        """Regions"""
        if ctx.invoked_subcommand is None:
            await self.bot.say("Please try again. You may have spelled something wrong")


    @regions.command(name="kanto", pass_context=True)
    async def _kanto(self,ctx):
        """The Kanto Region"""
        await self.bot.say("Hey " + ctx.message.author.mention + " here are the gyms for the **Kanto Region**.\n \n**__Pewter Gym__**\n```Type: Rock\nLeader: Sanderson536\nBadge: Boulder_Badge```\n**__Cerulean Gym__**\n```Type: Water\nLeader: Azure\nBadge: Cascade_Badge```\n**__Vermillion Gym__**\n```Type: Electric\nLeader: NONE\nBadge: Thunder_Badge```\n**__Fuchsia Gym__**\n```Type: Poison\nLeader: NONE\nBadge: Soul_Badge```\n**__Saffron Gym__**\n```Type: Psychic\nLeader: Mixi {👽 SaffronGL}{DayCare}\nBadge: Marsh_Badge```\n**__Cinnabar Gym__**\n```Type: Fire\nLeader: Me-Meow\nBadge: Volcano_Badge```\n**__Viridian GYm__**\n```Type: Ground\nLeader: Angelic Wolf\nBadge: Earth_Badge```\n**__Celadon Gym__**\n```Type: Grass\nLeader: BK\nBadge: Rainbow_Badge```")


def setup(bot):
    bot.add_cog(Regions(bot))