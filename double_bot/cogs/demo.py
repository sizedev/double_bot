import discord
from discord import app_commands
from discord.ext import commands

class DemoCog(commands.Cog):
    @app_commands.command(name="dash")
    async def dash(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello from the __bot__.")

    @commands.command(name="msg")
    async def msg(self, ctx: commands.Context):
        await ctx.send("This is a message command (they still exist!)")

    @app_commands.command(name="menu")
    async def menu(self, interaction: discord.Interaction):
        modal = discord.ui.Select(options = ["A", "B", "C"])
        await interaction.response.send_modal(modal=modal)
        await interaction.response.send_message(f"You selected: {modal.values}")

async def setup(bot):
    await bot.add_cog(DemoCog(bot))
