# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from importlib import reload
from typing import TYPE_CHECKING

from botbase import CogBase, MyContext
from nextcord.ext.commands import command, is_owner

from ..websocket import Manager

if TYPE_CHECKING:
    from minecat.__main__ import Minecat


class WebsocketManager(CogBase["Minecat"]):
    def __init__(self, bot: Minecat):
        super().__init__(bot)

        self.bot.manager = Manager(bot)

    @command()
    @is_owner()
    async def reload_manager(self, ctx: MyContext):
        from .. import websocket

        await ctx.send("Reloading module...")
        reload(websocket)
        await ctx.send("Reloaded module.")

        await ctx.send("Reloading extension...")
        self.bot.reload_extension("minecat.cogs.websocket.manager")
        await ctx.send("Reloaded extension.")


def setup(bot: Minecat):
    bot.add_cog(WebsocketManager(bot))
