import copy, os, json
import datetime
import traceback
from collections import Counter
from collections import OrderedDict

import discord
import psutil, aiohttp
from discord.ext import commands

from cogs.bot_utils import config, checks
from cogs.bot_utils.paginator import Pages
from colors import Colors


CARBONITEX_API = "https://www.carbonitex.net/discord/data/botdata.php"
DISCORDBOTS_PW = "https://bots.discord.pw/api"
DISCORDBOTS_ORG = "https://discordbots.org/api"


class Roles:
    """Commands for utilities related to Discord or the Bot itself."""

    def __init__(self, bot):
        self.bot = bot
        self.process = psutil.Process()
        self.config = config.Config('stats.json', loop=bot.loop, directory="data")
        self.session = aiohttp.ClientSession(loop=bot.loop)

    @commands.group(pass_context=True, no_pm=True, invoke_without_command=True)
    async def roles(self, ctx, *, member : discord.Member = None):
        """Shows info about a member.
        This cannot be used in private messages. If you don't specify
        a member then the info returned will be yours.
        """
        channel = ctx.message.channel
        if member is None:
            member = ctx.message.author

        e = discord.Embed()
        roles = [role.name.replace('@', '@\u200b') for role in member.roles]
        shared = sum(1 for m in self.bot.get_all_members() if m.id == member.id)
        voice = member.voice_channel
        if voice is not None:
            other_people = len(voice.voice_members) - 1
            voice_fmt = '{} with {} others' if other_people else '{} by themselves'
            voice = voice_fmt.format(voice.name, other_people)
        else:
            voice = 'Not connected.'

        e.set_author(name=str(member), icon_url=member.avatar_url or member.default_avatar_url)
        e.set_footer(text='Member since').timestamp = member.joined_at
        e.add_field(name='Server Role', value=member.top_role)
        e.add_field(name='Additional Roles', value=', '.join(roles))
        e.colour = member.colour

        if member.avatar:
            e.set_thumbnail(url=member.avatar_url)

        await self.bot.say(embed=e)

    @roles.command(name='server', pass_context=True, no_pm=True)
    async def server_info(self, ctx):
        server = ctx.message.server
        roles = [role.name.replace('@', '@\u200b') for role in server.roles]

        secret_member = copy.copy(server.me)
        secret_member.id = '0'
        secret_member.roles = [server.default_role]

        # figure out what channels are 'secret'
        secret_channels = 0
        secret_voice = 0
        text_channels = 0
        for channel in server.channels:
            perms = channel.permissions_for(secret_member)
            is_text = channel.type == discord.ChannelType.text
            text_channels += is_text
            if is_text and not perms.read_messages:
                secret_channels += 1
            elif not is_text and (not perms.connect or not perms.speak):
                secret_voice += 1

        voice_channels = len(server.channels) - text_channels
        member_by_status = Counter(str(m.status) for m in server.members)

        e = discord.Embed()
        e.title = 'This is ' + server.name
        e.add_field(name='Leader', value=server.owner)
        if server.icon:
            e.set_thumbnail(url=server.icon_url)

        if server.splash:
            e.set_image(url=server.splash_url)

        fmt = 'Text %s (%s secret)\nVoice %s (%s locked)'
        e.add_field(name='Channels', value=fmt % (text_channels, secret_channels, voice_channels, secret_voice))

        fmt = 'Total: {0}\nOnline: {1[online]}' \
              ', Offline: {1[offline]}' \
              '\nDnD: {1[dnd]}' \
              ', Idle: {1[idle]}'

        e.add_field(name='Members', value=fmt.format(server.member_count, member_by_status))
        e.add_field(name='Roles', value=', '.join(roles) if len(roles) < 10 else '%s roles' % len(roles))
        e.set_footer(text='Created').timestamp = server.created_at
        await self.bot.say(embed=e)


def setup(bot):
    bot.add_cog(Roles(bot))