import discord
from discord.ext import commands
import os
import sys

class Restart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Hybrid Command untuk restart
    @commands.hybrid_command(name="restart", with_app_command=True, description="Restart the bot (Hanya Admin dan Helper!)")
    @commands.is_owner()
    @commands.has_permissions(administrator=True)
    async def restart(self, ctx: commands.Context):
        embed = discord.Embed(
            title="Bot Restart",
            description="The bot is restarting...",
            color=discord.Color.darker_grey()
        )
        embed.set_footer(text="Please wait while the bot restarts.")
        
        # Send the embed message
        if isinstance(ctx, discord.Interaction):
            await ctx.send(embed=embed, ephemeral=True)
        else:
            await ctx.send(embed=embed)
        
        await self.bot.close()

        # Restart bot
        os.execv(sys.executable, ['python'] + sys.argv)

async def setup(bot):
    await bot.add_cog(Restart(bot))  # Menambahkan cog ke bot
