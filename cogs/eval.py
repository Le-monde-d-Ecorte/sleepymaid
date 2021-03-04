from discord.ext import commands
import discord

class eval(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['exec', 'evaluate'])
    @commands.is_owner()
    async def eval(self, ctx, *, args):
        result = exec(args)
        await ctx.send(f"```{result}```")

def setup(bot):
    bot.add_cog(eval(bot))
