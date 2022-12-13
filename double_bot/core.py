import logging
import os

import discord
from discord.ext import commands

from digiformatter import logger as digilogger

from double_bot.botutils import load_extensions

# Set up logging
logger: logging.Logger = None
discordlogger: logging.Logger = None

def setup_logging():
    global logger, discordlogger
    logging.basicConfig(level=logging.INFO)
    dfhandler = digilogger.DigiFormatterHandler()
    dfhandlersource = digilogger.DigiFormatterHandler(showsource=True)

    logger = logging.getLogger("double_bot")
    logger.setLevel(logging.DEBUG)
    logger.handlers = []
    logger.propagate = False
    logger.addHandler(dfhandler)

    discordlogger = logging.getLogger("discord")
    discordlogger.setLevel(logging.WARN)
    discordlogger.handlers = []
    discordlogger.propagate = False
    discordlogger.addHandler(dfhandlersource)

def run_bot():
    setup_logging()
    intents = discord.Intents.all()
    bot = DoubleBot(command_prefix=["?"], intents=intents)
    bot.run(os.environ['BOT_TOKEN'], log_handler = None)

class DoubleBot(commands.Bot):
    async def setup_hook(self):
        DOUBLE_SCORE_GUILD=discord.Object(id=1050992474283319366)
        await load_extensions(self, "double_bot.cogs")
        # To sync global commands, just drop the guild parameter. But global commands take several hours to sync new commands, so this way is best in testing.
        await self.tree.sync(guild=DOUBLE_SCORE_GUILD)

    async def on_ready(self):
        print("Beepity Boopity")
