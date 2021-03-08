import discord

from io import BytesIO
from utils import default
from discord.ext import commands

class drrazz_events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        if guild.id == 818313526720462868:
            channel = guild.get_channel(818313526720462870)
            embed = discord.Embed(description=f"Bievenue {member.mention} sur {guild.name}.", colour=discord.Colour(0x36393f))
            embed.set_author(name="Nouveau Membres", icon_url="https://cdn.discordapp.com/emojis/612355003151286278.gif")
            await channel.send(embed)

def setup(bot):
    bot.add_cog(drrazz_events(bot))
