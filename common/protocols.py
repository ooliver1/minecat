# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Coroutine

from orjson import dumps, loads
from websockets.client import WebSocketClientProtocol
from websockets.exceptions import ConnectionClosedOK
from websockets.server import WebSocketServerProtocol

if TYPE_CHECKING:
    from logging import Logger
    from typing import AsyncIterator

    from .types import JsonType


__all__ = ("JsonWebSocketServer", "JsonWebSocketClient")


# The mro hates me no matter what I do :(
class JsonWebSocketServer(WebSocketServerProtocol):
    logger: Logger

    def send(self, message: JsonType) -> Coroutine[Any, Any, None]:  # type: ignore
        return super().send(dumps(message).decode())

    async def recv(self) -> JsonType:  # type: ignore  # would like to override
        return loads(await super().recv())

    async def __aiter__(self) -> AsyncIterator[JsonType]:  # type: ignore
        try:
            while True:
                yield loads(await super().recv())
        except ConnectionClosedOK:
            return


# HACK: I absolutely hate this but for some reason they will not overwrite
WebSocketServerProtocol.__aiter__ = JsonWebSocketServer.__aiter__  # type: ignore


class JsonWebSocketClient(WebSocketClientProtocol):
    def send(self, message: JsonType) -> Coroutine[Any, Any, None]:  # type: ignore [imcompatible-override]
        return super().send(dumps(message).decode())

    async def recv(self) -> JsonType:  # type: ignore [imcompatible-override]
        return loads(await super().recv())

    async def __aiter__(self) -> AsyncIterator[JsonType]:  # type: ignore [imcompatible-override]
        try:
            while True:
                yield await self.recv()
        except ConnectionClosedOK:
            return


# HACK: I absolutely hate this but for some reason they will not overwrite
WebSocketClientProtocol.__aiter__ = JsonWebSocketClient.__aiter__  # type: ignore
