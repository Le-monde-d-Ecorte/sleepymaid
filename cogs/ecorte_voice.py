import discord
import discord.utils

from io import BytesIO
from utils import default
from discord.ext import commands

serverid = 324284116021542922 # Le monde d'Ecorte
en_vocal_role = 821791970632400956 # -- vocal -- Le monde d'Ecorte
dans_un_vocal_role = 784121432811634760 # Dans un vocal Le monde d'Ecorte
voice_log_channel_id = 821509142518824991 # voice_log Le monde d'Ecorte

class ecorte_voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
# Join un vocal
        if before.channel is None and after.channel is not None:
            if after.channel.guild.id != serverid:
                return
            guild = after.channel.guild
            voicelogchannel = guild.get_channel(voice_log_channel_id)

            embed = discord.Embed(title="Presence Update", description=f"**{member.name}#{member.discriminator}** has joined **{after.channel.name}**.", color=0x419400)
            await voicelogchannel.send(embed=embed)

            # give role en vocal

            lignerole = guild.get_role(en_vocal_role)
            dansunvocalrole = guild.get_role(dans_un_vocal_role)
            await member.add_roles(lignerole, reason=f"Joined a voice channel. ({after.channel.name})")
            await member.add_roles(dansunvocalrole, reason=f"Joined a voice channel. ({after.channel.name})")


# leave un vocal
        elif after.channel is None and before.channel is not None:
            if before.channel.guild.id != serverid:
                return
            guild = before.channel.guild
            voicelogchannel = guild.get_channel(voice_log_channel_id)

            embed = discord.Embed(title="Presence Update", description=f"**{member.name}#{member.discriminator}** has left **{before.channel.name}**.", color=0x419400)
            await voicelogchannel.send(embed=embed)

            # remove role en vocal

            lignerole = guild.get_role(en_vocal_role)
            dansunvocalrole = guild.get_role(dans_un_vocal_role)
            await member.remove_roles(lignerole, reason=f"Left a voice channel. ({before.channel.name})")
            await member.remove_roles(dansunvocalrole, reason=f"Left a voice channel. ({before.channel.name})")

# Switch de vocal
        elif before.channel != after.channel:
            if after.channel.guild.id != serverid:
                return
            guild = before.channel.guild
            voicelogchannel = guild.get_channel(voice_log_channel_id)

            embed = discord.Embed(title="Presence Update", description=f"**{member.name}#{member.discriminator}** has moved from **{before.channel.name}** to **{after.channel.name}**.", color=0x419400)
            await voicelogchannel.send(embed=embed)

def setup(bot):
    bot.add_cog(ecorte_voice(bot))
