import discord
from discord.ext import commands
from .utils import checks
import aiohttp
import asyncio

class Roleadd:
	def __init__(self, bot):
		self.bot = bot
		self.discord = __import__('discord')

	#def on_member_join(self, member):
	#	role = self.discord.utils.get(server.roles, name="Member")
	#	await bot.add_roles(member, role)
	@checks.is_owner()
	@commands.command(pass_context=True, no_pm=True)
	async def addrole(self, ctx, member : discord.Member):
		server = ctx.message.server
		role = discord.utils.get(server.roles, id="247190206770315264")
		await self.bot.add_roles(member, role)
def setup(bot):
	bot.add_cog(Roleadd(bot))