# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import TYPE_CHECKING

from common.protocols import JsonWebSocketServer

from .opcode import Opcode

if TYPE_CHECKING:
    from .errors import ServerError
    from common.types import JsonType


class WebSocketServer(JsonWebSocketServer):
    uuid: str

    async def send_error(self, error: ServerError) -> None:
        self.logger.error("Error occured! %s: %s", error, error.__doc__)
        payload: JsonType = {}

        data: JsonType = {}

        data["exc"] = error.value
        data["msg"] = error.__doc__

        payload["o"] = Opcode.ERROR.value
        payload["d"] = data

        await self.send(payload)
