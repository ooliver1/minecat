# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from common import JsonWebSocketClient
from mineager import Opcode

__all__ = ("MinecatWebSocketClient",)


class MinecatWebSocketClient(JsonWebSocketClient):
    async def login(self, cluster: int) -> None:
        await self.send({"o": Opcode.LOGIN.value, "d": cluster})
