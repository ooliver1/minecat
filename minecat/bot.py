# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from asyncio import TimeoutError as AsyncTimeoutError
from asyncio import create_task, gather, sleep, wait_for
from contextlib import suppress
from logging import getLogger
from typing import TYPE_CHECKING

from botbase import BotBase
from nextcord import shard
from nextcord.gateway import DiscordWebSocket
from redis.asyncio import Redis

if TYPE_CHECKING:
    from asyncio import Future
    from typing import Any, Coroutine

log = getLogger(__name__)
__all__ = ("Minecat",)


class Shard(shard.Shard):
    async def reidentify(self, exc: shard.ReconnectWebSocket) -> None:
        if exc.op == "RESUME":
            self._client.dispatch("shard_resuming", self.id)

        await super().reidentify(exc)


class Minecat(BotBase):
    def __init__(self, *args, current_cluster: int, **kwargs):
        super().__init__(*args, **kwargs)
        self.keydb = Redis(host="keydb", port=6379)
        self._waiting_futures: dict[int, Future[None]] = {}
        self.cluster_id = current_cluster

    async def close(self):
        with suppress(AsyncTimeoutError):
            await wait_for(self.keydb.close(), timeout=5)

    async def start(self, *args: Any, **kwargs: Any):
        create_task(self._handle_shard_messages())

        await super().start(*args, **kwargs)

    async def _handle_shard_messages(self):
        assert self.shard_ids is not None

        pubsub = self.keydb.pubsub()
        await pubsub.subscribe(*(f"queue:{i}" for i in self.shard_ids))

        async for message in pubsub.listen():
            log.debug("Got message %s", message)

            if message["type"] != "message":
                continue

            shard_id = int(message["channel"].decode().split(":")[1])

            if shard_id not in self._waiting_futures:
                continue

            log.info("Got the OK for shard %s", shard_id)

            self._waiting_futures[shard_id].set_result(None)
            del self._waiting_futures[shard_id]

    async def launch_shard(
        self, gateway: str, shard_id: int, *, initial: bool = False
    ) -> None:
        fut = self.loop.create_future()
        self._waiting_futures[shard_id] = fut
        log.info("Waiting for shard %s in the queue", shard_id)
        await self.keydb.publish(f"shards:{shard_id}", "WAITING")
        await fut

        try:
            self.dispatch("shard_connecting", shard_id)
            coro = DiscordWebSocket.from_client(
                self, initial=initial, gateway=gateway, shard_id=shard_id
            )
            ws = await wait_for(coro, timeout=180.0)
        except Exception:
            log.error("Failed to connect for shard_id: %s. Retrying...", shard_id)
            await sleep(5)
            return await self.launch_shard(gateway, shard_id)

        # Yes private attributes.
        self._AutoShardedClient__shards[shard_id] = ret = Shard(  # pyright: ignore
            ws, self, self._AutoShardedClient__queue.put_nowait  # pyright: ignore
        )
        ret.launch()

    async def launch_shards(self) -> None:
        if self.shard_count is None:
            self.shard_count, gateway = await self.http.get_bot_gateway()
        else:
            gateway = await self.http.get_gateway()

        self._connection.shard_count = self.shard_count

        shard_ids = self.shard_ids or range(self.shard_count)
        self._connection.shard_ids = shard_ids

        tasks: list[Coroutine[Any, Any, None]] = []
        for shard_id in shard_ids:
            initial = shard_id == shard_ids[0]
            tasks.append(self.launch_shard(gateway, shard_id, initial=initial))

        await gather(*tasks)

        self._connection.shards_launched.set()

    async def on_shard_connecting(self, shard_id: int):
        await self.keydb.publish(f"shards:{shard_id}", "CONNECTING")

    async def on_shard_connect(self, shard_id: int):
        await self.keydb.publish(f"shards:{shard_id}", "CONNECTED")

    async def on_shard_ready(self, shard_id: int):
        await self.keydb.publish(f"shards:{shard_id}", "READY")

    async def on_shard_resuming(self, shard_id: int):
        await self.keydb.publish(f"shards:{shard_id}", "RESUMING")

    async def on_shard_disconnect(self, shard_id: int):
        await self.keydb.publish(f"shards:{shard_id}", "DISCONNECTED")

    async def on_ready(self):
        log.info("Shards %s in cluster %s are ready!", self.shard_ids, self.cluster_id)
