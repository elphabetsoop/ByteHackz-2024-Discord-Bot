from typing import Type
from dis_snek.models import Scale
from dis_snek.models.application_commands import (
    OptionTypes,
    slash_command,
    component_callback,
    slash_option,
)
from dis_snek.models.command import message_command
from dis_snek.models.context import InteractionContext
from dis_snek.models.discord_objects.embed import EmbedAttachment
from dis_snek.models.discord_objects.embed import Embed
from dis_snek.models.discord_objects.components import Button
from dis_snek.models.discord_objects.embed import Embed
from dis_snek.models.enums import ButtonStyles

from utils.config import GUILD
from discord.utils import get


class Welcome(Scale):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="welcome", description="It's time for Bytehackz 2024!")
    async def welcome(self, ctx: InteractionContext):
        embed = Embed(

            "Hello and welcome to Bytehackz 2024!",
            "The Byte®Hackz is an annual hackathon conducted for Information Technology students taking the module Full Stack Development Project (FSDP).\n\n\
            There will be 7 challenge statements, with 5 Groups of 4 to 5 Participants attempting each challenge statement.",
            color="#F9AC42",
            image="https://media.discordapp.net/attachments/1294543462292521010/1302153434610270279/BANNER.png?ex=67271463&is=6725c2e3&hm=e474046bfd8ee6cf9f90e7e5922a9d2069c28eb7aa8e1a2760f181c8ce9aa211&=&format=webp&quality=lossless&width=1146&height=565"
        )

        await ctx.send(embeds=[embed])

        print("DEBUG: Welcome command executed")
        # await ctx.send("https://cdn.discordapp.com/attachments/895590724836401175/904702785965150278/unknown.png")
        await ctx.send(
            "Welcome to Bytehackz 2024, Claim your participant role here!",
            components=[
                Button(
                    style=ButtonStyles.BLURPLE,
                    label="Claim Role",
                    #emoji=":computer:",
                    custom_id="claimRole",
                )
            ],
        )
        
        print("DEBUG: Sent claimrole")

    @component_callback("claimRole")
    async def claimRole(self, ctx):

        guild = await self.bot.get_guild(GUILD)
        role = get(guild.roles, name="Byte®Hackz Participants")
        if (ctx.author.has_role(role)):
            await ctx.send("Already Claimed Role", ephemeral=True)
        else:
            await ctx.author.add_role(role)
            await ctx.send("Sucessfully claimed role, Welcome To Bytehackz 2024!", ephemeral=True)


def setup(bot):
    Welcome(bot)
