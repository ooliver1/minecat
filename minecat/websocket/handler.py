# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from websockets.server import WebSocketServerProtocol

log = getLogger(__name__)
__all__ = ("ws_handler",)


async def ws_handler(websocket: WebSocketServerProtocol) -> None:
    path = websocket.path
    path = path.removeprefix("/?guild_id=")
    log.info(f"Connected to guild {path}")

    if path.isdigit():
        guild_id = int(path)
        log.info(f"Guild ID: {guild_id}")
    else:
        log.info("Invalid guild ID, closing connection")
        await websocket.close()
        return

    async for message in websocket:
        log.debug("Received message: %s", message)
