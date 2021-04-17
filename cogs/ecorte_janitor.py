import discord
import time

from utils import default
from discord.ext import commands
from utils import permissions, default, http

guild_id = 324284116021542922


class ecorte_janitor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    def is_in_guild(guild_id):
        async def predicate(ctx):
            return ctx.guild and ctx.guild.id == guild_id
        return commands.check(predicate)

#    @commands.Cog.listener()
#    async def on_message(self, message):
#        guild = message.guild
#        member = message.author
#        if isinstance(message.channel, discord.DMChannel):
#            return
#        if message.guild.id != guild_id:
#            return
#        if message.author.bot:
#            return
#        if message.channel.id in [439155130924007444, 816419654205177857, 816419626576511016, 777648765065625670, 817135816564015104, 781651409023533117, 793247248033120266]:
#            return
#        nouveau_role = guild.get_role(614126210422800404)
#        membres_role = guild.get_role(823227863284449352)
#        rainbow_role = guild.get_role(818207098877116417)
#        key_role = guild.get_role(827237537222230056)
#        has_nouveau = False
#        has_membres = False
#        has_level_role = False
#        has_noexp = False
#        has_other_acces_role = False
#        is_not_eligible_for_rainbow = True
#        has_key = False
#        has_rainbow = False
#        member_roles = message.author.roles
#        for index, role in enumerate(member_roles):
#            if role.name.lower() == 'nouveau':
#                has_nouveau = True
#            elif role.name.lower() == 'membres':
#                has_membres = True
#            elif role.name.lower() == 'no-exp':
#                has_noexp = True
#            elif role.name.lower() in ['actif', 'normal', 'habituer', 'addicte', 'insomniaque', 'pas de vie']:
#                has_level_role = True
#            elif role.name.lower() in ['no-exp', 'addicte', 'insomniaque', 'pas de vie', 'nitro booster']:
#                is_not_eligible_for_rainbow = False
#            elif role.name.lower() in ['irl', 'ancien staff', 'staff en pause']:
#                has_other_acces_role = True
#            elif role.name.lower() == '🔑':
#                has_key = True
#            elif role.name.lower() == 'rainbow':
#                has_rainbow = True
#        if has_membres and has_nouveau:
#            await member.remove_roles(nouveau_role)
#            await message.channel.send(f"L'utilisateur <@{member.id}> a level up de Nouveaux à Membres.")
#        if has_level_role and has_nouveau:
#            await member.remove_roles(nouveau_role)
#            await message.channel.send(f"L'utilisateur <@{member.id}> a level up de Nouveaux à un rôle plus haut.")
#        if has_noexp and has_nouveau:
#            await member.remove_roles(nouveau_role)
#        if has_key and has_membres:
#            await member.remove_roles(key_role)
#        if has_key and has_level_role:
#            await member.remove_roles(key_role)
#        if has_rainbow:
#            if is_not_eligible_for_rainbow:
#                await member.remove_roles(rainbow_role)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        guild = after.guild
        member = after
        if guild.id != guild_id:
            return
        if member.bot:
            return
        nouveau_role = guild.get_role(614126210422800404)
#        membres_role = guild.get_role(823227863284449352)
        rainbow_role = guild.get_role(818207098877116417)
        key_role = guild.get_role(827237537222230056)
        has_nouveau = False
        has_membres = False
        has_level_role = False
        has_noexp = False
        is_not_eligible_for_rainbow = True
        has_key = False
        has_rainbow = False
        member_roles = member.roles
        for index, role in enumerate(member_roles):
            if role.name.lower() == 'nouveau':
                has_nouveau = True
            elif role.name.lower() == 'membres':
                has_membres = True
            elif role.name.lower() == 'no-exp':
                has_noexp = True
            elif role.name.lower() in ['actif', 'normal', 'habituer', 'addicte', 'insomniaque', 'pas de vie']:
                has_level_role = True
            elif role.name.lower() in ['no-exp', 'addicte', 'insomniaque', 'pas de vie', 'nitro booster', 'mods', 'rainbow bypass']:
                is_not_eligible_for_rainbow = False
            elif role.name.lower() == '🔑':
                has_key = True
            elif role.name.lower() == 'rainbow':
                has_rainbow = True
        if has_membres and has_nouveau:
            await member.remove_roles(nouveau_role)
#            await message.channel.send(f"L'utilisateur <@{member.id}> a level up de Nouveaux à Membres.")
        if has_level_role and has_nouveau:
            await member.remove_roles(nouveau_role)
#            await message.channel.send(f"L'utilisateur <@{member.id}> a level up de Nouveaux à un rôle plus haut.")
        if has_noexp and has_nouveau:
            await member.remove_roles(nouveau_role)
        if has_key and has_membres:
            await member.remove_roles(key_role)
        if has_key and has_level_role:
            await member.remove_roles(key_role)
        if has_key and has_nouveau:
            await member.remove_roles(nouveau_role)
        if has_rainbow:
            if is_not_eligible_for_rainbow:
                await member.remove_roles(rainbow_role)

    @commands.command()
    @is_in_guild(324284116021542922)
    @commands.check(permissions.is_owner)
    async def month_end(self, ctx):
        key_role = ctx.guild.get_role(827237537222230056)
        nouveau_role = ctx.guild.get_role(614126210422800404)
        for index, member in enumerate(key_role.members):
            await member.remove_roles(key_role)
            await member.add_roles(nouveau_role)
        time.sleep(2)
        membres_role = ctx.guild.get_role(823227863284449352)
        for index, member in enumerate(membres_role.members):
            await member.remove_roles(membres_role)
            await member.add_roles(key_role)
        time.sleep(2)
        actif_role = ctx.guild.get_role(823228233025323038)
        for index, member in enumerate(actif_role.members):
            await member.remove_roles(actif_role)
            await member.add_roles(key_role)
        time.sleep(2)
        normal_role = ctx.guild.get_role(823228560193486938)
        for index, member in enumerate(normal_role.members):
            await member.remove_roles(normal_role)
            await member.add_roles(key_role)
        time.sleep(2)
        habituer_role = ctx.guild.get_role(823228994462941184)
        for index, member in enumerate(habituer_role.members):
            await member.remove_roles(habituer_role)
            await member.add_roles(key_role)
        time.sleep(2)
        addicte_role = ctx.guild.get_role(823233856776699944)
        for index, member in enumerate(addicte_role.members):
            await member.remove_roles(addicte_role)
            await member.add_roles(key_role)
        time.sleep(2)
        insomniaque_role = ctx.guild.get_role(823302261354659850)
        for index, member in enumerate(insomniaque_role.members):
            await member.remove_roles(insomniaque_role)
            await member.add_role(key_role)
        time.sleep(2)
        pas_de_vie_role = ctx.guild.get_role(823302283788812319)
        for index, member in enumerate(pas_de_vie_role.members):
            await member.remove_roles(pas_de_vie_role)
            await member.add_roles(key_role)
        print("month_end")

    @commands.command()
    @is_in_guild(324284116021542922)
    @commands.check(permissions.is_owner)
    async def announce_winner(self, ctx, winner: discord.Member):
        channel = ctx.guild.get_channel(809468282520338432)
        await channel.send(f"> **Nouveau Mois**\n> **1er Avril 2021**\n\n**Membre du mois: <@{winner.id}>**, Il obtient donc le rôle <@&817570082330378250>.\n-	Se qui donne accès a la commande ``!motm`` pour voir tous les commandes qui débloque en étant membre du mois.\n\n:small_orange_diamond: Pour être membre du mois tu doit être premier dans le leaderboard Amari. Pour voir ton rank va dans <#439155130924007444> et fait ``;rank``.")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        if member.bot:
            return
        if guild.id == guild_id:
            generalchannel = guild.get_channel(436249478521946191)
            await generalchannel.send(f":arrow_right: {member.mention}")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = member.guild
        if member.bot:
            return
        if guild.id == guild_id:
            generalchannel = guild.get_channel(436249478521946191)
            await generalchannel.send(f":arrow_left: {member.name}")


def setup(bot):
    bot.add_cog(ecorte_janitor(bot))
