# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import TYPE_CHECKING, AsyncIterator, Awaitable, Callable

from common import JsonWebSocketServer

if TYPE_CHECKING:
    from .types import ManagerJsonType


class ClusteredWebSocketServer(JsonWebSocketServer):
    cluster: int
    recv: Callable[[], Awaitable[ManagerJsonType]]  # type: ignore [incompatible-override]
    __aiter__: Callable[[], AsyncIterator[ManagerJsonType]]  # type: ignore [incompatible-override]
