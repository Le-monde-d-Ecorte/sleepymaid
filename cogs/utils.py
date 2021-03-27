import discord
import requests
import json

from discord.ext import commands
from utils import lists, permissions, http, default, argparser

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @commands.command()
    async def pronoun(self, ctx, user: discord.Member = None):
        """ See your prounouns or someone pronouns. (Powered by pronoundb.org) """
        good_version = {
            "unspecified": "Unspecified",
            "hh": "He/Him",
            "hi": "He/It",
            "hs": "He/She",
            "ht": "He/They",
            "ih": "It/Him",
            "ii": "It/Its",
            "is": "It/She",
            "it": "It/They",
            "shh": "She/He",
            "sh": "She/Her",
            "si": "She/It",
            "st": "She/They",
            "th": "They/He",
            "ti": "They/It",
            "ts": "They/She",
            "tt": "They/Them",
            "any": "Any pronouns",
            "other": "Other pronouns",
            "ask": "Ask me my pronouns",
            "avoid": "Avoid pronouns, use my name"
        }
        if not user:
            user = ctx.author
        else:
            user = user
        try:
            url = 'https://pronoundb.org/api/v1/lookup'
            response = requests.get(url, params={'platform': "discord", 'id': user.id})
            data = response.json()
            to_send_pronoun = good_version[data['pronouns']]
            embed = discord.Embed(title=f"{user}'s pronouns:", colour=discord.Colour(0x36393f), description=f"{to_send_pronoun}")
            embed.set_footer(text="Data provided by https://pronoundb.org/")
            await ctx.send(embed=embed)
        except KeyError:
            await ctx.send(f"{user.name}#{user.discriminator} does not appear to have any pronouns set. Please tell them to go to https://pronoundb.org/ and set their pronouns.")

def setup(bot):
    bot.add_cog(Utils(bot))
