import discord
from discord import app_commands
from discord.ext import commands

class DemoCog(commands.Cog):
    @app_commands.command(name="dash")
    async def dash(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello from the __bot__.")

async def setup(bot):
    await bot.add_cog(DemoCog(bot))
