import discord

from utils import default
from discord.ext import commands

guild_id = 324284116021542922
crown_role_id = 817570082330378250

class ecorte_motm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    def is_in_guild(guild_id):
        async def predicate(ctx):
            return ctx.guild and ctx.guild.id == guild_id
        return commands.check(predicate)

    @commands.group()
    @is_in_guild(324284116021542922)
    async def motm(self, ctx):
        """ La commande de base pour le membre du mois. """
        crown_role = ctx.guild.get_role(crown_role_id)
        if crown_role in ctx.author.roles:
            if ctx.invoked_subcommand is None:
                await ctx.send_help(str(ctx.command))
        else:
            await ctx.send("> :x: Tu doit être le membre du mois pour utiliser cette commande.")

    @motm.command(name="nom", aliases=["n", "name"])
    @commands.cooldown(1, 60, commands.BucketType.guild)
    @is_in_guild(324284116021542922)
    async def nom(self, ctx, *, name: str):
        """ Changer le nom du rôle. """
        crown_role = ctx.guild.get_role(crown_role_id)
        if crown_role in ctx.author.roles:
            await crown_role.edit(name=f"{name} ᴹᴼᵀᴹ")
            await ctx.reply("> :white_check_mark: Nom modifié!", mention_author=True)
        else:
            await ctx.reply("> :x: Tu doit être le membre du mois pour utiliser cette commande.", mention_author=True)

    @motm.command(name="couleur", aliases=["c", "color", "colour"])
    @commands.cooldown(1, 60, commands.BucketType.guild)
    @is_in_guild(324284116021542922)
    async def couleur(self, ctx, color_input: discord.Colour = None):
        """ Changer la couleur du rôle. """
        crown_role = ctx.guild.get_role(crown_role_id)
        if crown_role in ctx.author.roles:
            if not color_input:
                await crown_role.edit(colour=0)
                await ctx.reply("> :white_check_mark: Couleur modifié!", mention_author=True)
            else:
                await crown_role.edit(colour=color_input)
                await ctx.reply("> :white_check_mark: Couleur modifié!", mention_author=True)
        else:
            await ctx.reply("> :x: Tu doit être le membre du mois pour utiliser cette commande.", mention_author=True)


def setup(bot):
    bot.add_cog(ecorte_motm(bot))
