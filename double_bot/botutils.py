from pathlib import Path

from discord.ext import commands

# Added a util to load all extensions in a particular directory
async def load_extensions(bot: commands.Bot, pkg: str):
    path = Path(pkg.replace(".", "/"))
    for extpath in path.glob("*.py"):
        cog = f"{pkg}.{extpath.stem}"
        print(cog)
        await bot.load_extension(cog)