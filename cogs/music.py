import discord
import DiscordUtils
import re
import asyncio

from discord.ext import commands
# from discord.voice_client import VoiceClient
from utils import permissions, default

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()
        music = DiscordUtils.Music()

    @commands.command()
    @commands.guild_only()
    async def join(ctx):
        """ Join your voice channel """
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                raise InvalidVoiceChannel('No channel to join. Please either specify a valid channel or join one.')

        vc = ctx.voice_client

        if vc:
            if vc.channel.id == channel.id:
                return
            try:
                await vc.move_to(channel)
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Moving to channel: <{channel}> timed out.')
        else:
            try:
                await channel.connect()
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Connecting to channel: <{channel}> timed out.')

        await ctx.send(f'Connected to: **{channel}**', delete_after=20)

def setup(bot):
    bot.add_cog(Music(bot))
