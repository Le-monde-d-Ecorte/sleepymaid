import discord

from time import time
from utils import default
from discord.ext import commands
from utils import permissions, default, http


class eval(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @commands.command()
    @commands.guild_only()
    async def eval(self, ctx, *, args):
        result = exec(args)
        await ctx.send(result)


def setup(bot):
    bot.add_cog(eval(bot))
