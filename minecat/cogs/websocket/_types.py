# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from typing import Awaitable, Callable

from websockets.server import WebSocketServerProtocol

__all__ = ("JsonType", "WebSocketCallback")

json_types = str | int | float | bool | None
InternalType = json_types | list["InternalType"] | dict[str, "InternalType"]
JsonType = dict[str, "InternalType"]
WebSocketCallback = Callable[[WebSocketServerProtocol, JsonType], Awaitable[None]]
