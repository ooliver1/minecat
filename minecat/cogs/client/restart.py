# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import TYPE_CHECKING

from botbase import CogBase, MyContext
from nextcord.ext.commands import command
from mineager import Opcode

if TYPE_CHECKING:
    from minecat.__main__ import Minecat

    Context = MyContext[Minecat]


class Restart(CogBase["Minecat"]):
    @command()
    async def restart(self, ctx: Context, cluster_id: int):
        await self.bot.mnws.send({"o": Opcode.RESTART, "d": cluster_id})

        if cluster_id == -1:
            await ctx.send("Sent request to restart all")
        else:
            await ctx.send(f"Sent request to restart cluster {cluster_id}")


def setup(bot: Minecat):
    bot.add_cog(Restart(bot))
