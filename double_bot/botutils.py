import logging
from pathlib import Path

from discord.ext import commands

logger = logging.getLogger("double_bot")

# Added a util to load all extensions in a particular directory
async def load_extensions(bot: commands.Bot, pkg: str):
    path = Path(pkg.replace(".", "/"))
    for extpath in path.glob("*.py"):
        cog = f"{pkg}.{extpath.stem}"
        logger.debug(f"Loaded cog: {cog}")
        await bot.load_extension(cog)