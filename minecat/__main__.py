# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from asyncio import set_event_loop_policy
from os import getenv, environ as env

from botbase import BotBase
from dotenv import load_dotenv
from nextcord import Intents, MemberCacheFlags
from uvloop import EventLoopPolicy


set_event_loop_policy(EventLoopPolicy())
load_dotenv()
shard_total = int(env["SHARD_TOTAL"])
shard_start = int(env["SHARD_START"])
shard_count = int(env["SHARD_COUNT"])
shard_ids = list(range(shard_start, shard_start + shard_count))


class MyBot(BotBase):
    # mcws: WebSocketServer

    # async def startup(self, *args, **kwargs):
    #     self.mcws = await run()

    #     await super().startup(*args, **kwargs)
    ...


intents = Intents.none()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
intents.members = True
bot = MyBot(
    intents=intents,
    member_cache_flags=MemberCacheFlags.none(),
    shard_ids=shard_ids,
    shard_count=shard_total,
)


bot.run(getenv("TOKEN"))
