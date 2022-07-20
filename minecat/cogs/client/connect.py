# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from botbase import CogBase
from orjson import loads
from websockets.client import connect, WebSocketClientProtocol
from websockets.exceptions import ConnectionClosed

if TYPE_CHECKING:
    from minecat.__main__ import Minecat
    from ..websocket import JsonType


log = getLogger(__name__)


class Connect(CogBase["Minecat"]):
    def __init__(self, bot: Minecat) -> None:
        super().__init__(bot)

        bot.loop.create_task(self.connect())

    async def connect(self) -> None:
        async for ws in connect("ws://manager:6420"):
            try:
                async for message in ws:
                    await self.handler(ws, loads(message))
            except ConnectionClosed:
                continue

    async def handler(self, ws: WebSocketClientProtocol, message: JsonType) -> None:
        log.debug("Received message from manager: %s", message)


def setup(bot: Minecat):
    bot.add_cog(Connect(bot))
