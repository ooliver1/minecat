# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from logging import getLogger

from websockets.server import serve

from ..config import version
from .handler import ws_handler

log = getLogger(__name__)

__all__ = ("run",)


async def run() -> None:
    async with serve(
        ws_handler,
        host="0.0.0.0",
        port=6969,
        logger=log,
        extra_headers={"X-Minecat-Version": version},
    ) as websocket_server:
        await websocket_server.wait_closed()
