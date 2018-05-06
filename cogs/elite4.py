import discord
from discord.ext import commands

class Donation:
    """Gives the link to KetchumMaps donation page."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def elite4(self,ctx):
        """Gives the link to KetchumMaps donation page."""
        await self.bot.say("Hey " + ctx.message.author.mention + " We are so glad you are interested in the Elite 4 unfortunately it's not ready yet")
    
    @commands.command(pass_context=True)
    async def pokeleague(self,ctx):
        """Shows the badges"""

        # Command function
        await self.bot.say("Hey " + ctx.message.author.mention + " Pokemon League will be here soon!")

    @commands.command(pass_context=True)
    async def tournaments(self,ctx):
        """Tournaments? What? Welcome to the newest feature"""
        
        # Command function
        await self.bot.say("Hey " + ctx.message.author.mention + " First tournament is now underway in <#435086774000287766> and <#435087192289705984> stay tuned for more information!")

    @commands.command(pass_context=True)
    async def helpme(self,ctx):
        """Shows the badges"""

        # Command function
        await self.bot.say("Hey " + ctx.message.author.mention + "Before asking for help please refer to <#434304246276685825> or <#433740903027572736> If you did not find your answer there then proceed to ask your question. **Do not DM any Mods at any time unless approved before hand**.")


def setup(bot):
    bot.add_cog(Donation(bot))