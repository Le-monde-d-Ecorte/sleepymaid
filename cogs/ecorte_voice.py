import discord
import discord.utils

from io import BytesIO
from utils import default
from discord.ext import commands

serverid = 324284116021542922 # Le monde d'Ecorte
en_vocal_role = 821791970632400956 # -- vocal -- Le monde d'Ecorte
dans_un_vocal_role = 784121432811634760 # Dans un vocal Le monde d'Ecorte
voice_log_channel_id = 821509142518824991 # voice_logs Le monde d'Ecorte

in_voice_channel_list = [
    662113104951377960, # 0 Bureau d'Ecorte
    816414942474928198, # 1 Staff
    818300783078146049, # 2 En live
    809932718820425728, # 3 Valorant
    485528168401338371, # 4 IRL
    617339537957453834, # 5 Public 1
    617339691146018866, # 6 Public 2
    811002839228219432, # 7 Level 1+
    815439982273626182, # 8 Level 5+
    817147513354059877, # 9 Level 20+
    699722283794563144, # 10 AFK
    787059609302073344 # 11 Rejoint
]

class ecorte_voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        class invoice_role:
            async def add_role(channel):
                guild = after.channel.guild
                # Bureau d'Ecorte
                if channel == in_voice_channel_list[0]:
                    role = guild.get_role(597479857940725761)
                # Staff
                if channel == in_voice_channel_list[1]:
                    role = guild.get_role(822248947166609438)
                # En live
                if channel == in_voice_channel_list[2]:
                    role = guild.get_role(822249421592330270)
                # Valorant
                if channel == in_voice_channel_list[3]:
                    role = guild.get_role(822250135480041484)
                # IRL
                if channel == in_voice_channel_list[4]:
                    role = guild.get_role(822250136268570674)
                # Public 1
                if channel == in_voice_channel_list[5]:
                    role = guild.get_role(822250138654867486)
                # Public 2
                if channel == in_voice_channel_list[6]:
                    role = guild.get_role(822251710038278154)
                # Level 1+
                if channel == in_voice_channel_list[7]:
                    role = guild.get_role(822251715273293866)
                # Level 5+
                if channel == in_voice_channel_list[8]:
                    role = guild.get_role(822251718502776833)
                # Level 20+
                if channel == in_voice_channel_list[9]:
                    role = guild.get_role(822251721195520020)
                # Level 20+
                if channel == in_voice_channel_list[10]:
                    role = guild.get_role(822251724156305448)

                lignerole = guild.get_role(en_vocal_role)
                dansunvocalrole = guild.get_role(dans_un_vocal_role)
                await member.add_roles(role, lignerole, dansunvocalrole, reason=f"Joined a voice channel. ({after.channel.name})")
            async def remove_role(channel):
                guild = before.channel.guild
                # Bureau d'Ecorte
                if channel == in_voice_channel_list[0]:
                    role = guild.get_role(597479857940725761)
                # Staff
                if channel == in_voice_channel_list[1]:
                    role = guild.get_role(822248947166609438)
                # En live
                if channel == in_voice_channel_list[2]:
                    role = guild.get_role(822249421592330270)
                # Valorant
                if channel == in_voice_channel_list[3]:
                    role = guild.get_role(822250135480041484)
                # IRL
                if channel == in_voice_channel_list[4]:
                    role = guild.get_role(822250136268570674)
                # Public 1
                if channel == in_voice_channel_list[5]:
                    role = guild.get_role(822250138654867486)
                # Public 2
                if channel == in_voice_channel_list[6]:
                    role = guild.get_role(822251710038278154)
                # Level 1+
                if channel == in_voice_channel_list[7]:
                    role = guild.get_role(822251715273293866)
                # Level 5+
                if channel == in_voice_channel_list[8]:
                    role = guild.get_role(822251718502776833)
                # Level 20+
                if channel == in_voice_channel_list[9]:
                    role = guild.get_role(822251721195520020)
                # Level 20+
                if channel == in_voice_channel_list[10]:
                    role = guild.get_role(822251724156305448)

                lignerole = guild.get_role(en_vocal_role)
                dansunvocalrole = guild.get_role(dans_un_vocal_role)
                await member.remove_roles(role, lignerole, dansunvocalrole, reason=f"Left a voice channel. ({before.channel.name})")

        # Join un vocal
        if before.channel is None and after.channel is not None:
            if after.channel.guild.id != serverid:
                return
            guild = after.channel.guild
            voicelogchannel = guild.get_channel(voice_log_channel_id)

            embed = discord.Embed(title="Presence Update", description=f"**{member.name}#{member.discriminator}** has joined **{after.channel.name}**.", color=0x419400, timestamp=embed.created_at)
            await voicelogchannel.send(embed=embed)

            # utiliser la class in_voice_role

            await invoice_role.add_role(after.channel.id)

        # leave un vocal
        elif after.channel is None and before.channel is not None:
            if before.channel.guild.id != serverid:
                return
            guild = before.channel.guild
            voicelogchannel = guild.get_channel(voice_log_channel_id)

            embed = discord.Embed(title="Presence Update", description=f"**{member.name}#{member.discriminator}** has left **{before.channel.name}**.", color=0x419400, timestamp=embed.created_at)
            await voicelogchannel.send(embed=embed)

            # utiliser la class in_voice_role

            await invoice_role.remove_role(before.channel.id)

            # remove role en vocal



        # Switch de vocal
        elif before.channel != after.channel:
            if after.channel.guild.id != serverid:
                return
            guild = before.channel.guild
            voicelogchannel = guild.get_channel(voice_log_channel_id)

            embed = discord.Embed(title="Presence Update", description=f"**{member.name}#{member.discriminator}** has moved from **{before.channel.name}** to **{after.channel.name}**.", color=0x419400, timestamp=embed.created_at)
            await voicelogchannel.send(embed=embed)

            # utiliser la class in_voice_role

            await invoice_role.add_role(after.channel.id)
            await invoice_role.remove_role(before.channel.id)


def setup(bot):
    bot.add_cog(ecorte_voice(bot))
