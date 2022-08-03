# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from common import JsonWebSocketServer

__all__ = ("UUIDWebSocketServer",)


class UUIDWebSocketServer(JsonWebSocketServer):
    uuid: str
