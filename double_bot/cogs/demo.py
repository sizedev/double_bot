import discord
from discord import app_commands, SelectOption
from discord.ui import Select, Modal
from discord.ext import commands

class Menu(Modal, title="Menu"):
    select = Select(options = [SelectOption(label="A"), SelectOption(label="B"), SelectOption(label="C")])
    
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected: {self.select.values}")


class DemoCog(commands.Cog):
    @app_commands.command(name="dash")
    async def dash(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello from the __bot__.")

    @commands.command(name="msg")
    async def msg(self, ctx: commands.Context):
        await ctx.send("This is a message command (they still exist!)")

    @app_commands.command(name="menu")
    async def menu(self, interaction: discord.Interaction):
        await interaction.response.send_modal(Menu())

async def setup(bot: commands.Bot):
    await bot.add_cog(DemoCog(bot))
