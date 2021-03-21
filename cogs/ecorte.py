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
            ctx.send("Tu doit avoir le rôle Rainbow.")

def setup(bot):
    bot.add_cog(ecorte(bot))
