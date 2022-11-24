# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import TYPE_CHECKING

from redis.asyncio import Redis

if TYPE_CHECKING:
    from asyncio import Event

__all__ = ("Manager",)


class Manager:
    def __init__(self, *, event: Event):
        self.keydb = Redis(host="keydb", port=6379)
        self.event = event

    async def start(self):
        pass

    async def close(self):
        self.event.set()
        await self.keydb.close()
