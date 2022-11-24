# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from asyncio import TimeoutError as AsyncTimeoutError
from asyncio import wait_for
from contextlib import suppress
from os import getenv

from botbase import BotBase
from redis.asyncio import Redis

from .utils import INTENTS, SHARD_IDS, TOTAL_SHARDS, MEMBER_CACHE_FLAGS


class Minecat(BotBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keydb = Redis(host="keydb", port=6379)

    async def close(self):
        with suppress(AsyncTimeoutError):
            await wait_for(self.keydb.close(), timeout=5)

        await self.keydb.close()


bot = Minecat(
    intents=INTENTS,
    member_cache_flags=MEMBER_CACHE_FLAGS,
    shard_ids=SHARD_IDS,
    shard_count=TOTAL_SHARDS,
)


bot.run(getenv("TOKEN"))
