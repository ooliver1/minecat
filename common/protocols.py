# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import TYPE_CHECKING, Awaitable
from abc import ABC

from orjson import dumps
from websockets.server import WebSocketServerProtocol
from websockets.client import WebSocketClientProtocol
from websockets.legacy.protocol import WebSocketCommonProtocol

if TYPE_CHECKING:
    from .types import JsonType


__all__ = ("JsonWebSocketServer", "JsonWebSocketClient")


class JsonMixin(WebSocketCommonProtocol):
    def send_json(self, json: JsonType) -> Awaitable[None]:
        return self.send(dumps(json).decode())


class JsonWebSocketServer(JsonMixin, WebSocketServerProtocol):
    ...


class JsonWebSocketClient(JsonMixin, WebSocketClientProtocol):
    ...
