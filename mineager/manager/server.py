# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import TYPE_CHECKING
from ssl import SSLContext

from websockets.server import serve

from .protocol import ClusteredWebSocketServer
from .handler import handle

if TYPE_CHECKING:
    from websockets.typing import LoggerLike
    from websockets.legacy.server import Serve

__all__ = ("run_manager",)


def run_manager(
    *, host: str, port: int, ssl: SSLContext | None, logger: LoggerLike | None
) -> Serve:
    return serve(
        ws_handler=handle,  # type: ignore
        host=host,
        port=port,
        ssl=ssl,
        logger=logger,
        create_protocol=ClusteredWebSocketServer,  # type: ignore  # websockets pls fix
    )
