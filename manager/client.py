# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from asyncio import create_task
from logging import getLogger
from typing import TYPE_CHECKING

from redis.asyncio import Redis

from .logs import set_logging
from .utils import Limiter

if TYPE_CHECKING:
    from asyncio import AbstractEventLoop, Event
    from typing import Literal

    ShardState = Literal[
        "WAITING", "CONNECTING", "CONNECTED", "READY", "RESUMING", "DISCONNECTED"
    ]

__all__ = ("Manager",)

set_logging()
log = getLogger(__name__)


class Manager:
    def __init__(self, *, event: Event, loop: AbstractEventLoop):
        self.keydb = Redis(host="keydb", port=6379)
        self.pubsub = self.keydb.pubsub()
        self.event = event
        self.shard_queue = Limiter(1, 5, identifier="shard-queue", loop=loop)

    async def start(self):
        log.info("Starting manager")
        create_task(self.handle_shards())

    async def close(self):
        self.event.set()
        await self.keydb.close()

    async def handle_shards(self):
        log.info("Subscribing to shard channels")
        await self.pubsub.psubscribe("shards:*")

        async for message in self.pubsub.listen():
            log.debug("Received data %s", message)

            if message["type"] in ("message", "pmessage"):
                state: ShardState = message["data"].decode()

                await self.handle_shard(
                    channel=message["channel"].decode(), state=state
                )

    async def handle_shard(self, *, channel: str, state: ShardState):
        _, shard_id = channel.split(":")

        if state == "WAITING":
            create_task(self.queue_shard(shard_id))
        elif state == "CONNECTING":
            log.info("Shard %s is connecting", shard_id)
        elif state == "CONNECTED":
            log.info("Shard %s is connected", shard_id)
        elif state == "READY":
            log.info("Shard %s is ready", shard_id)
        elif state == "RESUMING":
            log.info("Shard %s is resuming", shard_id)
        elif state == "DISCONNECTED":
            log.info("Shard %s is disconnected", shard_id)
        else:
            log.warning("Unknown state %s", state)

    async def queue_shard(self, shard_id: str):
        log.info("Queueing shard %s", shard_id)

        async with self.shard_queue:
            log.info("Obtained queue for shard %s", shard_id)
            await self.keydb.publish(f"queue:{shard_id}", "OK")
