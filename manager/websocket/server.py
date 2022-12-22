# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from logging import getLogger

from websockets.server import serve

from common import Websocket

from .handler import ws_handler

log = getLogger(__name__)

__all__ = ("run",)


async def run() -> None:
    async with serve(
        ws_handler,  # type: ignore
        host="0.0.0.0",
        port=6899,
        logger=log,
        create_protocol=Websocket,
    ) as websocket_server:
        await websocket_server.wait_closed()
