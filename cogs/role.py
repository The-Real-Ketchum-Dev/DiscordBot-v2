import discord
from discord.ext import commands


class teams:
    """Teams in discord!"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def team(self, ctx):
        user = ctx.message.author
        server = ctx.message.server
        roles = [role.name.replace('@', '@\u200b') for role in user.roles]
        if 'team' in roles:
            await self.bot.say("You already joined that team!")
            await self.bot.say("You have already joined a team please leave a team before adding a new one")
        else:
            serverroles = [role.name.replace('@', '@\u200b') for role in server.roles]
            if 'Team' in serverroles:
                team = discord.utils.find(lambda r: r.name == 'Team', ctx.message.server.roles)
                await self.bot.add_roles(user, team)
                await self.bot.say("Join Success! :+1:")

            else:
                await self.bot.say("No roles found, creating them now.... ")
                team = await self.bot.create_role(ctx.message.server)
                await self.bot.edit_role(ctx.message.server, team, name='Team', colour=discord.Colour(value=5020550))
    
    @commands.command(pass_context=True, no_pm=True)
    async def battle(self, ctx):
        user = ctx.message.author
        server = ctx.message.server
        roles = [role.name.replace('@', '@\u200b') for role in user.roles]
        if 'Battle' in roles:
            await self.bot.say("You already joined that team!")
            await self.bot.say("You have already joined a team please leave a team before adding a new one")
        else:
            serverroles = [role.name.replace('@', '@\u200b') for role in server.roles]
            if 'Battle' in serverroles:
                team = discord.utils.find(lambda r: r.name == 'Team', ctx.message.server.roles)
                await self.bot.add_roles(user, team)
                await self.bot.say("Join Success! :+1:")

            else:
                await self.bot.say("No roles found, creating them now.... ")
                team = await self.bot.create_role(ctx.message.server)
                battle = await self.bot.create_role(ctx.message.server)
                await self.bot.edit_role(ctx.message.server, team, name='Team', colour=discord.Colour(value=5020550))
                await self.bot.edit_role(ctx.message.server, team, name='Battle', colour=discord.Colour(value=2059292))

    @commands.group(name='roleleave', pass_context=True, no_pm=True)
    async def _roleleave(self, ctx):
        """Leave a pokemon go team"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)
            return

    @_roleleave.command(name='team', pass_context=True, no_pm=True)
    async def _team(self, ctx):
        server = ctx.message.server
        user = ctx.message.author
        serverroles = [role.name.replace('@', '@\u200b') for role in server.roles]
        roles = [role.name.replace('@', '@\u200b') for role in user.roles]
        team = discord.utils.find(lambda r: r.name == 'Team', ctx.message.server.roles)
        if 'Team' in serverroles:
            if 'Team' in roles:
                await self.bot.remove_roles(user, team)
                await self.bot.say("Succesfuly left team :+1:")
            else:
                await self.bot.say("You have not joined that team!")
        else:
            await self.bot.say("Please run the join command for first time configuration")

    @_roleleave.command(name='battle', pass_context=True, no_pm=True)
    async def _battle(self, ctx):
        server = ctx.message.server
        user = ctx.message.author
        serverroles = [role.name.replace('@', '@\u200b') for role in server.roles]
        roles = [role.name.replace('@', '@\u200b') for role in user.roles]
        team = discord.utils.find(lambda r: r.name == 'Battle', ctx.message.server.roles)
        if 'Team' in serverroles or 'Battle' in serverroles:
            if 'battle' in roles:
                await self.bot.remove_roles(user, team)
                await self.bot.say("Succesfuly left team :+1:")
            else:
                await self.bot.say("You have not joined that team!")
        else:
            await self.bot.say("Please run the join command for first time configuration")


def setup(bot):
    n = teams(bot)
    bot.add_cog(n)
