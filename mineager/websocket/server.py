# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import TYPE_CHECKING
from ssl import SSLContext

from websockets.server import serve

from .handler import handle

if TYPE_CHECKING:
    from common import LoggerLike
    from websockets.legacy.server import Serve

__all__ = ("run_ws",)


def run_ws(
    *, host: str, port: int, ssl: SSLContext | None, logger: LoggerLike | None
) -> Serve:
    return serve(ws_handler=handle, host=host, port=port, ssl=ssl, logger=logger)
