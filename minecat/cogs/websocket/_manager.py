# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import TYPE_CHECKING

from ._errors import ServerError
from ._opcode import Opcode

if TYPE_CHECKING:
    from minecat.__main__ import Minecat
    from ._server import WebSocketServer

    from common.types import JsonType, WebSocketCallback

__all__ = ("Manager",)


class Manager:
    def __init__(self, bot: Minecat) -> None:
        self.bot = bot
        self.callbacks: dict[Opcode, WebSocketCallback] = {}

    async def __call__(self, *, ws: WebSocketServer, data: JsonType) -> None:
        ws.logger.debug("Handling and finding opcode")

        if "o" not in data:
            return await ws.send_error(ServerError.MISSING_OPCODE)

        raw_opcode = data["o"]

        try:
            opcode = Opcode(raw_opcode)
        except ValueError:
            return await ws.send_error(ServerError.UNKNOWN_OPCODE)

        callback = self.callbacks.get(opcode)

        if callback is None:
            return ws.logger.error("No callback for opcode %s", opcode)

        ws.logger.debug("Found callback for opcode %s", opcode)
        await callback(ws, data)
