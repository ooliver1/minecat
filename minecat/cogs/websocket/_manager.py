# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from logging import getLogger

from typing import TYPE_CHECKING

from ._errors import ServerError
from ._opcode import Opcode

if TYPE_CHECKING:
    from minecat.__main__ import Minecat
    from ._types import WebSocketCallback, JsonType
    from ._server import WebSocketServer


log = getLogger(__name__)


class Manager:
    def __init__(self, bot: Minecat) -> None:
        self.bot = bot
        self.callbacks: dict[Opcode, WebSocketCallback]

    async def __call__(self, *, ws: WebSocketServer, data: JsonType) -> None:
        if "opcode" not in data:
            await ws.send_error(ServerError.MISSING_OPCODE)
        if (opcode := data["o"]) not in Opcode:
            await ws.send_error(ServerError.UNKNOWN_OPCODE)

        callback = self.callbacks.get(Opcode(data["opcode"]))

        if callback is None:
            return log.error("No callback for opcode %s", opcode)

        await callback(ws, data)
