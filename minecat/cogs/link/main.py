# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import TYPE_CHECKING

from botbase import CogBase, MyInter
from nextcord import SlashOption, slash_command

if TYPE_CHECKING:
    from minecat.__main__ import Minecat


class Link(CogBase["Minecat"]):
    LINK_UUID_DESC = (
        "The UUID of your server, shown in the console and plugins/minecat/uuid.txt"
    )

    @slash_command()
    async def link(self, _):
        ...

    @link.subcommand(description="Link your Minecraft server to minecat!")
    async def server(
        self, inter: MyInter, uuid: str = SlashOption(description=LINK_UUID_DESC)
    ):
        ...


def setup(bot: Minecat):
    bot.add_cog(Link(bot))
