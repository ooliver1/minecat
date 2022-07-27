# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from ssl import SSLContext
from typing import TYPE_CHECKING

from websockets.server import serve

from .handler import handle
from .protocol import ClusteredWebSocketServer

if TYPE_CHECKING:
    from logging import Logger, LoggerAdapter

    from websockets.legacy.server import Serve

    LoggerLike = Logger | LoggerAdapter[Logger]

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
