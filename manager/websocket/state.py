# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from asyncio import get_running_loop
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from asyncio import Future

    from common import Websocket

__all__ = ("State",)


class State:
    __slots__ = ("clients", "waiters", "loop")

    def __init__(self) -> None:
        self.clients: dict[str, Websocket[State]] = {}
        """uuid: client"""
        self.waiters: dict[str, Future[None]] = {}
        """uuid: waiter"""
        self.loop = get_running_loop()

    def hold_client(self, uuid: str) -> Future[None]:
        future = self.loop.create_future()
        self.waiters[uuid] = future

        return future
