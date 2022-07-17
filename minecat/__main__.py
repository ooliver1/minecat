# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from asyncio import set_event_loop_policy
from os import environ as env
from os import getenv
from typing import TYPE_CHECKING

from botbase import BotBase
from dotenv import load_dotenv
from nextcord import Intents, MemberCacheFlags
from uvloop import EventLoopPolicy

if TYPE_CHECKING:
    from websockets.server import WebSocketServer

    from .cogs.websocket import Manager

set_event_loop_policy(EventLoopPolicy())
load_dotenv()
shard_total = int(env["SHARD_TOTAL"])
shard_start = int(env["SHARD_START"])
shard_count = int(env["SHARD_COUNT"])
shard_ids = list(range(shard_start, shard_start + shard_count))
cluster = int((shard_total / shard_count) * (shard_start / shard_total))
"""THe current cluster id (indexed from 0)

cluster count                 position in cluster "line"
---------------------------------------------------------
( ( 6 / 3 ) = 2 (clusters)  *  ( 0 / 6 ) = 0 (position out of 1)) = 0 (cluster id)
( ( 6 / 3 ) = 2 (clusters)  *  ( 3 / 6 ) = 0.5 (position out of 1)) = 1 (cluster id)
"""


class Minecat(BotBase):
    manager: Manager
    mcws: WebSocketServer
    cluster: int


intents = Intents.none()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
intents.members = True
bot = Minecat(
    intents=intents,
    member_cache_flags=MemberCacheFlags.none(),
    shard_ids=shard_ids,
    shard_count=shard_total,
)
bot.cluster = cluster


bot.run(getenv("TOKEN"))
