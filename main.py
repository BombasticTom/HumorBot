# DAY 1: Make a discord bot that should order a pizza using shadows (ShadowMario's) debit card, delivered straight to their door - Riveren 2023
# DAY 2: Make it send a spooky image every time someone with #SHADOWCULT in their name sends a message - Riveren 2023

import discord
import os
import random

from discord.ext import commands
from source.Configuration import Configuration
from source.Humor import Humor
from source.Paths import Paths

class Client(commands.Bot):
    # A lil class i made for managing the bot easier
    def __init__(self, cmdprf: str, dcIntents: discord.Intents):
        # Initializing stuff (not important)
        super().__init__(command_prefix = cmdprf, intents = dcIntents())
        self.cogsToLoad = [file[:-3] for file in os.listdir('./source/cogs') if file.endswith('.py')]

    async def setup_hook(self):
        # Loads cogs
        for ext in self.cogsToLoad:
            await self.load_extension(f'source.cogs.{ext}')

    async def on_ready(self):
        # Notifies the owner that the client is ready for use
        print(f'{client.user} is ready to go!')

    async def on_message(self, message: discord.Message):
        if message.author.bot: return # Verifies if the message sender isn't the client itself
        # Checks if your bot is mentioned in the message context, including words "order pizza"
        if self.user.mentioned_in(message=message) and "order pizza" in message.content.lower():
            # Initiate funny 🤣!
            await message.reply(
                f"Just ordered pizza using ShadowMario's {abs(random.randrange(0, 100, 10)-1)}.99$ {random.choice(Humor.popularPlatforms)} "
                f"giftcard! The code was `{Humor.giftcardGenerator()}`.\n"
                f"The delivery has been scheduled. I am going to find you in... {Humor.formatTime(random.randint(1, 7201))}!"
            )
        # Checks if you're in ShadowMario's cult and if you've mentioned riveren.
        if 'riveren' in message.content.lower() and '#shadowcult' in message.author.display_name.lower():
            # Initiate scary 😱!
            await message.reply(
                "Boo! Did I scare you?! 😹", file = discord.File(Paths.image("riveren"))
            )

# Running the custom Bot Client class
client = Client(";", discord.Intents.all)
client.run(Configuration.TOKEN)