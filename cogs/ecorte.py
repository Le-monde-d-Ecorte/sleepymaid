import discord
import random

from utils import default
from discord.ext import commands

class ecorte(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    def is_in_guild(guild_id):
        async def predicate(ctx):
            return ctx.guild and ctx.guild.id == guild_id
        return commands.check(predicate)

    @commands.command(hidden=True, aliases=['vc', 'vraimentcouleur', 'rb'])
    @commands.cooldown(1, 300, commands.BucketType.user)
    @is_in_guild(324284116021542922)
    async def rainbow(self, ctx):
        role = ctx.guild.get_role(818207098877116417)
        if role in ctx.author.roles:
            r = random.randint(1, 16777215)
            await role.edit(color=r)
            cc = role.colour
            embed=discord.Embed(description=f"Tu viens de changer la couleur du rôle <@&818207098877116417> pour {cc}. \nTu peut rechanger la couleur du rôle <@&818207098877116417> dans 5 minutes. \nPour avoir la couleur retire tout tes rôles de couleur/couleur de rôle custom.", color=r)
            embed.set_author(name="Rôle Rainbow", icon_url="https://media.discordapp.net/attachments/811959848921071636/822598144968884314/baa392758f065fa770e3a9063f91d33a.png")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Tu doit avoir le rôle Rainbow.")

    @commands.command(hidden=True, aliases=['v'])
    @is_in_guild(324284116021542922)
    async def verify(self, ctx, user: discord.Member):
        staffrole = ctx.guild.get_role(797650029278920714)
        if staffrole in ctx.author.roles:
            userrole = ctx.guild.get_role(614126210422800404)
            infoligne = ctx.guild.get_role(784120538896531456)
            autreligne = ctx.guild.get_role(788167400096792577)
            lvlligne = ctx.guild.get_role(823226227224477717)
            await user.add_roles(userrole, infoligne, autreligne, lvlligne, reason=f"Manually got verified by {ctx.author.name}#{ctx.author.discriminator}")
            await ctx.reply(":white_check_mark: Done!", mention_author=False)

    @commands.command(hidden=True, aliases=['uv'])
    @is_in_guild(324284116021542922)
    async def unverify(self, ctx, user: discord.Member):
        staffrole = ctx.guild.get_role(797650029278920714)
        if staffrole in ctx.author.roles:
            userrole = ctx.guild.get_role(614126210422800404)
            infoligne = ctx.guild.get_role(784120538896531456)
            autreligne = ctx.guild.get_role(788167400096792577)
            lvlligne = ctx.guild.get_role(823226227224477717)
            await user.remove_roles(userrole, infoligne, autreligne, lvlligne, reason=f"Manually got un-verified by {ctx.author.name}#{ctx.author.discriminator}")
            await ctx.reply(":white_check_mark: Done!", mention_author=False)

    @commands.command(hidden=True)
    @is_in_guild(324284116021542922)
    async def noexp(self, ctx):
        membrerole = ctx.guild.get_role(823227863284449352)
        noexprole = ctx.guild.get_role(823229487974055957)
        if ctx.channel != 796886716719562762:
            await ctx.reply(":x: Wrong channel.", mention_author=False)
        if membrerole in ctx.author.roles:
            await ctx.author.add_roles(noexprole)
            await ctx.author.remove_roles(membrerole)
            await ctx.reply(":white_check_mark: Done!", mention_author=False)

    @commands.command(hidden=True, aliases=['ap'])
    @is_in_guild(324284116021542922)
    async def approve(self, ctx, member: discord.Member):
        staffrole = ctx.guild.get_role(797650029278920714)
        approvedrole = ctx.guild.get_role(823691168982237185)
        if staffrole in ctx.author.roles:
            await member.add_roles(approvedrole, reason=f"Manually got approved by {ctx.author.name}#{ctx.author.discriminator})
            await ctx.reply(":white_check_mark: Done!", mention_author=False)

def setup(bot):
    bot.add_cog(ecorte(bot))
