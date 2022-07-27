# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import TYPE_CHECKING

from nextcord import slash_command
from botbase import CogBase, MyInter

if TYPE_CHECKING:
    from minecat.__main__ import Minecat


class Link(CogBase["Minecat"]):
    @slash_command()
    async def link(self, _):
        ...

    @link.subcommand()
    async def server(self, inter: MyInter):
        ...


def setup(bot: Minecat):
    bot.add_cog(Link(bot))
