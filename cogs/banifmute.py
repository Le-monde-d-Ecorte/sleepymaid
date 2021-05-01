import discord

from discord.ext import commands
from utils import default

whitelisted_guild = [
    324284116021542922
]


class banifmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()
        self._last_result = None

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id in whitelisted_guild:
            for index, role in enumerate(member.roles):
                if role.name.lower() == 'muted':
                    await member.guild.ban(
                        member, reason="[ AutoBan ] Leaving while muted...", delete_message_days=0)


def setup(bot):
    bot.add_cog(banifmute(bot))
