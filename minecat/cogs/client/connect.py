# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from botbase import CogBase
from mineager import Opcode
from minecat.client import MinecatWebSocketClient
from websockets.client import connect
from websockets.exceptions import ConnectionClosed

if TYPE_CHECKING:
    from common import JsonType
    from minecat.__main__ import Minecat

log = getLogger(__name__)


class Connect(CogBase["Minecat"]):
    def __init__(self, bot: Minecat) -> None:
        super().__init__(bot)

        bot.loop.create_task(self.connect())

    async def connect(self) -> None:
        async for ws in connect(  # type: ignore  # should be correct type
            "ws://manager:6420",
            create_protocol=MinecatWebSocketClient,  # type: ignore  # doesnt know how to type
        ):
            ws: MinecatWebSocketClient
            self.bot.mnws = ws
            await ws.login(self.bot.cluster)
            try:
                async for message in ws:
                    await self.handler(ws, message)
            except ConnectionClosed:
                continue

    async def handler(self, ws: MinecatWebSocketClient, message: JsonType) -> None:
        log.debug("Received message from manager: %s", message)
        opcode = Opcode(message["o"])

        if opcode == Opcode.RESTART:
            await self.bot.close()


def setup(bot: Minecat):
    bot.add_cog(Connect(bot))
