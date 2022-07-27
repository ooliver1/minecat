# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from logging import Logger, LoggerAdapter
from typing import Awaitable, Callable, TYPE_CHECKING

from websockets.server import WebSocketServerProtocol

if TYPE_CHECKING:
    LoggerAdapter = LoggerAdapter[Logger]

__all__ = ("JsonType", "WebSocketCallback", "LoggerLike")

json_types = str | int | float | bool | None
InternalType = json_types | list["InternalType"] | dict[str, "InternalType"]
JsonType = dict[str, "InternalType"]
WebSocketCallback = Callable[[WebSocketServerProtocol, JsonType], Awaitable[None]]
LoggerLike = Logger | LoggerAdapter
