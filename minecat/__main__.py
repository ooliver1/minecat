# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license


from asyncio import gather
from logging import getLogger
from os import getenv

from .bot import Minecat
from .utils import CURRENT_CLUSTER, INTENTS, MEMBER_CACHE_FLAGS, SHARD_IDS, TOTAL_SHARDS
from .websocket import run as run_ws

log = getLogger(__name__)


bot = Minecat(
    intents=INTENTS,
    member_cache_flags=MEMBER_CACHE_FLAGS,
    shard_ids=SHARD_IDS,
    shard_count=TOTAL_SHARDS,
    current_cluster=CURRENT_CLUSTER,
)


async def main():
    await gather(bot.start(getenv("TOKEN")), run_ws())


# ":(( future from other loop :((" - asyncio 2022
bot.loop.run_until_complete(main())
