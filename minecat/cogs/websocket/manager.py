# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from importlib import reload
from typing import TYPE_CHECKING

from botbase import CogBase, MyContext as Context
from minecat.websocket import Manager
from nextcord.ext.commands import command

if TYPE_CHECKING:
    from minecat.__main__ import Minecat

    Context = Context[Minecat]


class WebsocketManager(CogBase["Minecat"]):
    @command()
    async def reload_manager(self, ctx: Context):
        from ... import websocket

        await ctx.send("Reloading module...")
        reload(websocket.manager)
        reload(websocket)
        await ctx.send("Reloaded module.")

        await ctx.send("Reloading extension...")
        self.bot.reload_extension("minecat.cogs.websocket.manager")
        await ctx.send("Reloaded extension.")


def setup(bot: Minecat):
    bot.add_cog(WebsocketManager(bot))
    bot.manager = Manager(bot)
