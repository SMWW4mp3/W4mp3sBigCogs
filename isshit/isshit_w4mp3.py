import random
import discord
import time
from discord.ext import commands
from __main__ import send_cmd_help, settings
from .utils.dataIO import dataIO

class Isshit:
    """Read the info.json for more informations."""

    def __init__(self, bot):
        self.bot = bot
        self.settings_path = "data/isshit_w4mp3"
        self.isshit = dataIO.load_json(self.settings_path + "/list.json")

    @commands.command()
    async def isshit(self, user : discord.Member):
        """Command insults the target in a even more creative way than !insult does."""
        if user.mention != "":
            await self.bot.say(random.choice(self.isshit).format(user.mention))
        else:
            await self.bot.say("You need to mention someone with @ for this command to work, knucklehead")

def setup(bot):
    bot.add_cog(Isshit(bot))
