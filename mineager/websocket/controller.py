# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from logging import getLogger
from typing import Awaitable, Callable

from .storage import storage

__all__ = ("Controller", "controller")
log = getLogger(__name__)


async def callback(uuid: str):
    ws = storage.get(uuid)

    if ws is not None:
        await ws.close(4100, "Reconnect to be assigned to a new node.")

        storage.pop(uuid, None)
    else:
        log.warning("Unable to drop %s, could not find client.", uuid)


class Controller:
    def __init__(self, *, ws_callback: Callable[[str], Awaitable[None]]) -> None:
        self.ws_callback = ws_callback

    async def drop_client(self, uuid: str) -> None:
        await self.ws_callback(uuid)


controller = Controller(ws_callback=callback)
