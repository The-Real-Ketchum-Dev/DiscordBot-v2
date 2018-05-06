import discord
from discord.ext import commands

class Battles:
    """Gives the link to KetchumMaps donation page."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def teams(self,ctx):
        """Just teams here"""
        await self.bot.say("Hey " + ctx.message.author.mention + " we are working on a new team feature.\nStay tuned.")

    @commands.group(invoke_without_command=True,pass_context=True)
    async def squads(self,ctx,teams):
        """Teams that are joinable"""
        if ctx.invoked_subcommand is None:
            await self.bot.say("Please try again. You may have spelled something wrong")


    @squads.command(name="team_rocket", invoke_without_command=True, pass_context=True)
    async def _team_rocket(self,ctx):
        """Team Rocket"""
        await self.bot.say("Join our team and steal Pikachu!!")


    @squads.command(name="harmony", invoke_without_command=True, pass_context=True)
    async def _harmony(self,ctx):
        """Team Harmony"""
        await self.bot.say("Join our team!!")


def setup(bot):
    bot.add_cog(Battles(bot))