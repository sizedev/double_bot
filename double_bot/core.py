import os

import discord
from discord.ext import commands

from double_bot.botutils import load_extensions

def run_bot():
    intents = discord.Intents.default()
    bot = DoubleBot(command_prefix=[], intents=intents)
    bot.run(os.environ['BOT_TOKEN'])

class DoubleBot(commands.Bot):
    async def setup_hook(self):
        DOUBLE_SCORE_GUILD=discord.Object(id=1050992474283319366)
        await load_extensions(self, "double_bot.cogs")
        # To sync global commands, just drop the guild parameter. But global commands take several hours to sync new commands, so this way is best in testing.
        await self.tree.sync(guild=DOUBLE_SCORE_GUILD)

    async def on_ready(self):
        print("Beepity Boopity")
