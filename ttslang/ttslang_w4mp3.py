import discord
from discord.ext import commands
from __main__ import send_cmd_help, settings
from .utils.dataIO import dataIO

try:
    from gtts import gTTS
    gTTS_avail = True
except:
    gTTS_avail = False

class TtsLang:
    """Extension to the [p]sfx thing by irdumb, tmerc and flabjax"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ttslang(self, ctx, langu: str):
        """Change TTS language.\n'list' - show all available languages\n'current' - Current TTS language"""
        sfx_cog = self.bot.get_cog("Sfx")
        tts = gTTS(text=".", lang=sfx_cog.language) # Workaround, whatever :)
        if (gTTS_avail == False):
            print("no gtts")
            return
        
        if (langu == "current"): 
            await self.bot.say("Currnet Language: " + tts.LANGUAGES[sfx_cog.language])
            return

        if (langu == "list"): 
            await self.bot.say("I've send you a list of all languages available as a PM, check your PMs :)")

            msg = "```TTS - Languages supported by Googles API:\n"
            lang_keys = sorted(tts.LANGUAGES.keys())
            
            for i in lang_keys:
                msg = msg + "\n" + i + " - " + tts.LANGUAGES[i]
            await self.bot.whisper(msg + "```")
            return
        
        # Test if language is available
        try:
            tts.LANGUAGES[langu]
        except:
            await self.bot.say("I don't know the language you specified.")
            return

        sfx_cog.language = langu
        await self.bot.say("Ok, changed to "+tts.LANGUAGES[langu]+".")

def setup(bot):
    bot.add_cog(TtsLang(bot))
