# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

import shortuuid

if TYPE_CHECKING:
    from common import Websocket

    from .state import State

log = getLogger(__name__)
__all__ = ("ws_handler",)


async def ws_handler(websocket: Websocket[State]) -> None:
    path = websocket.path
    guild, uuid = path.removeprefix("/?guild_id=").split("&uuid=")

    if guild == "unknown":
        if uuid == "unknown":
            uuid = shortuuid.uuid()
            await websocket.send_login(uuid=uuid)
            log.info("Sending uuid %s to client.", uuid)

        websocket.state.clients[uuid] = websocket
    else:
        log.warning("Why do we have uuid %s, they know the guild.", uuid)

    await websocket.state.hold_client(uuid=uuid)

    await websocket.close()
    return
