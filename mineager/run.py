# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import TYPE_CHECKING

from .websocket import run_ws
from .websocket import default_logger

if TYPE_CHECKING:
    from ssl import SSLContext

    from websockets.typing import LoggerLike
    from websockets.legacy.server import Serve


__all__ = ("run",)


def run(
    *,
    host: str = "0.0.0.0",
    port: int = 6899,
    ssl: SSLContext | None = None,
    logger: LoggerLike | None = default_logger,
) -> Serve:
    return run_ws(host=host, port=port, ssl=ssl, logger=logger)
