import discord

from utils import default
from discord.ext import commands

class ecorte_janitor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    def is_in_guild(guild_id):
        async def predicate(ctx):
            return ctx.guild and ctx.guild.id == guild_id
        return commands.check(predicate)

    @commands.Cog.listener()
    async def on_message(self, message):
        guild = message.guild
        member = message.author
        if guild.id != 324284116021542922:
            return
        if isinstance(message.channel, discord.DMChannel):
            return
        if message.author.bot:
            return
        nouveau_role = message.guild.get_role(614126210422800404)
        membres_role = message.guild.get_role(823227863284449352)
        has_nouveau = False
        has_membres = False
        has_level_role = False
        has_noexp = False
        has_other_acces_role = False
        member_roles = message.author.roles
        for index, role in enumerate(member_roles):
            if role.name.lower() == 'nouveau':
                has_nouveau = True
            elif role.name.lower() == 'no-exp':
                has_noexp = True
            elif role.name.lower() in ['actif', 'normal', 'habituer', 'addicte', 'insomniaque', 'pas de vie']:
                has_level_role = True
            elif role.name.lower() in ['irl', 'ancien staff', 'staff en pause']:
                has_other_acces_role = True
        if has_membres and has_nouveau:
            await message.author.remove_roles(nouveau_role)
            await message.channel.send(f"L'utilisateur <@{message.author.id}> a level up de Nouveaux à Membres.")
        if has_level_role and has_nouveau:
            await message.author.remove_roles(nouveau_role)
            await message.channel.send(f"L'utilisateur <@{message.author.id}> a level up de Nouveaux à un rôle plus haut.")
        if has_noexp and has_nouveau:
            await message.author.remove_roles(nouveaux_role)

def setup(bot):
    bot.add_cog(ecorte_janitor(bot))
