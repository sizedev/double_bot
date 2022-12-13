from discord.ext import commands

class ErrorHandlerCog(commands.Cog):
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error) -> None:
        await ctx.send("Something went wrong")

async def setup(bot):
    await bot.add_cog(ErrorHandlerCog(bot))
