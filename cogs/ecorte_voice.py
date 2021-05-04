import discord
import discord.utils
import datetime

from io import BytesIO
from utils import default, lists
from discord.ext import commands


def return_current_time():
    time = datetime.datetime.utcnow()
    return time.strftime('%A, %b %d %H:%M')

class ecorte_voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        class invoice_role:
            async def add_role(channel):
                if channel in lists.ecorte_voice_for_role:
                    role = after.channel.guild.get_role(
                        lists.ecorte_voice_for_role[channel])
                    await member.add_roles(role, reason=f"Joined a voice channel. ({after.channel.name})")

            async def remove_role(channel):
                if channel in lists.ecorte_voice_for_role:
                    role = before.channel.guild.get_role(
                        lists.ecorte_voice_for_role[channel])
                    await member.remove_roles(role, reason=f"Left a voice channel. ({before.channel.name})")

        # Join un vocal
        if before.channel is None and after.channel is not None:
            if after.channel.guild.id != lists.ecorte_serverid:
                return
            guild = after.channel.guild
            voicelogchannel = guild.get_channel(lists.ecorte_voice_log_channel_id)

            embed = discord.Embed(
                title="Presence Update", description=f"**{member.name}#{member.discriminator}** has joined **{after.channel.name}**.", color=0x419400)
            embed.set_footer(text=return_current_time())
            await voicelogchannel.send(embed=embed)

            # Invoice role

            lignerole = guild.get_role(lists.ecorte_en_vocal_role)
            dansunvocalrole = guild.get_role(lists.ecorte_dans_un_vocal_role)
            await member.add_roles(lignerole, dansunvocalrole, reason=f"Joined a voice channel. ({after.channel.name})")

            # utiliser la class in_voice_role

            await invoice_role.add_role(after.channel.id)

        # leave un vocal
        elif after.channel is None and before.channel is not None:
            if before.channel.guild.id != lists.ecorte_serverid:
                return
            guild = before.channel.guild
            voicelogchannel = guild.get_channel(lists.ecorte_voice_log_channel_id)

            embed = discord.Embed(
                title="Presence Update", description=f"**{member.name}#{member.discriminator}** has left **{before.channel.name}**.", color=0x419400)
            embed.set_footer(text=return_current_time())
            await voicelogchannel.send(embed=embed)

            # Invoice role

            lignerole = guild.get_role(lists.ecorte_en_vocal_role)
            dansunvocalrole = guild.get_role(lists.ecorte_dans_un_vocal_role)
            await member.remove_roles(lignerole, dansunvocalrole, reason=f"Left a voice channel. ({before.channel.name})")

            # utiliser la class in_voice_role

            await invoice_role.remove_role(before.channel.id)

        # Switch de vocal
        elif before.channel != after.channel:
            if after.channel.guild.id != lists.ecorte_serverid:
                return
            guild = before.channel.guild
            voicelogchannel = guild.get_channel(lists.ecorte_voice_log_channel_id)

            embed = discord.Embed(
                title="Presence Update", description=f"**{member.name}#{member.discriminator}** has moved from **{before.channel.name}** to **{after.channel.name}**.", color=0x419400)
            embed.set_footer(text=return_current_time())
            await voicelogchannel.send(embed=embed)

            # utiliser la class in_voice_role

            await invoice_role.remove_role(before.channel.id)
            await invoice_role.add_role(after.channel.id)


def setup(bot):
    bot.add_cog(ecorte_voice(bot))
