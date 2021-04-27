import discord

from utils import default
from discord.ext import commands
from utils import permissions, default, http

id_for_tc = {
    1: 826987813760925756,  # sb
    2: 811959848921071636,  # dev
    3: 790715612799172658,  # weeb
    4: 823893349109989421,  # discord
    5: 778418636431949834,  # arts
    6: 835985017988579368  # wynncraft
}


class ecorte_clubs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    def is_in_guild(guild_id):
        async def predicate(ctx):
            return ctx.guild and ctx.guild.id == guild_id
        return commands.check(predicate)

    @commands.group()
    @is_in_guild(324284116021542922)
    async def club(self, ctx):
        """ Commande pour les clubs """
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))

    @club.command(name="join")
    @is_in_guild(324284116021542922)
    async def join(self, ctx, id: int):
        """ Rejoindre un club. """
        if id in id_for_tc:
            tc = ctx.guild.get_channel(id_for_tc[id])
            await tc.set_permissions(ctx.author, read_messages=True)
            if ctx.channel.id == 826987630683226152:
                await ctx.message.delete(delay=6)
                await ctx.reply(f":white_check_mark:  **Tu as rejoint le club <#{tc.id}>!**", mention_author=True, delete_after=5)
            else:
                await ctx.reply(f":white_check_mark:  **Tu as rejoint le club <#{tc.id}>!**", mention_author=True)

    @club.command(name="leave")
    @is_in_guild(324284116021542922)
    async def leave(self, ctx, id: int):
        """ Quitter un club. """
        if id in id_for_tc:
            tc = ctx.guild.get_channel(id_for_tc[id])
            await tc.set_permissions(ctx.author, overwrite=None)
            if ctx.channel.id == 826987630683226152:
                await ctx.message.delete(delay=6)
                await ctx.reply(f":white_check_mark:  **Tu as quitter le club <#{tc.id}>!**", mention_author=True, delete_after=5)
            else:
                await ctx.reply(f":white_check_mark:  **Tu as quitter le club <#{tc.id}>!**", mention_author=True)

    @club.command(name="list")
    @is_in_guild(324284116021542922)
    async def list(self, ctx):
        await ctx.reply("```1: Hypixel Skyblock\n2: Dev Club\n3: Weeb Club\n4: Discord Club\n5: Arts Club\n6: Wynncraft Club```")


def setup(bot):
    bot.add_cog(ecorte_clubs(bot))
