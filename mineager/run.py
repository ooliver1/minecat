# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import TYPE_CHECKING

from .manager import default_logger as manager_default_logger
from .manager import run_manager
from .websocket import default_logger as ws_default_logger
from .websocket import run_ws

if TYPE_CHECKING:
    from ssl import SSLContext

    from common import LoggerLike
    from websockets.legacy.server import Serve


__all__ = ("run",)


def run(
    *,
    host: str = "0.0.0.0",
    ws_port: int = 6899,
    manager_port: int = 6420,
    ssl: SSLContext | None = None,
    ws_logger: LoggerLike | None = ws_default_logger,
    manager_logger: LoggerLike | None = manager_default_logger,
) -> tuple[Serve, Serve]:
    return (
        run_ws(host=host, port=ws_port, ssl=ssl, logger=ws_logger),
        run_manager(host=host, port=manager_port, ssl=ssl, logger=manager_logger),
    )
