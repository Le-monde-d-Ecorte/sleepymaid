import discord
import discord.utils

from io import BytesIO
from utils import default
from discord.ext import commands

serverid = 324284116021542922
en_vocal_role = 821725150118150164
voice_log_channel_id = 324284116021542922

class ecorte_voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
# Join un vocal
        if before.channel is None and after.channel is not None:
#            if after.channel.guild.id == serverid:
            guild = after.channel.guild
            voicelogchannel = guild.get_channel(voice_log_channel_id)

            embed = discord.Embed(title="Presence Update", description=f"**{member.name}#{member.discriminator}** has joined **{after.channel.name}**.", color=0x419400)
            await voicelogchannel.send(embed=embed)

            # give role en vocal

            role = guild.get_role(en_vocal_role)
            await member.add_roles(role)

# leave un vocal
        elif after.channel is None and before.channel is not None:
            guild = before.channel.guild
            voicelogchannel = guild.get_channel(voice_log_channel_id)

            embed = discord.Embed(title="Presence Update", description=f"**{member.name}#{member.discriminator}** has left **{before.channel.name}**.", color=0x419400)
            await voicelogchannel.send(embed=embed)

            # remove role en vocal

            role = guild.get_role(en_vocal_role)
            await member.remove_roles(role)

# Switch de vocal
        elif before.channel != after.channel:
            guild = before.channel.guild
            voicelogchannel = guild.get_channel(voice_log_channel_id)

            embed = discord.Embed(title="Presence Update", description=f"**{member.name}#{member.discriminator}** has moved from **{before.channel.name}** to **{after.channel.name}**.", color=0x419400)
            await voicelogchannel.send(embed=embed)

def setup(bot):
    bot.add_cog(ecorte_voice(bot))
