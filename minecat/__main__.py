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
from minecat.websocket import WebSocketServer
from common import JsonWebSocketClient

if TYPE_CHECKING:
    from nextcord.ext.commands import Context

    from .websocket import Manager

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


log = __import__("logging").getLogger(__name__)


class Minecat(BotBase):
    manager: Manager
    mcws: WebSocketServer
    mnws: JsonWebSocketClient
    cluster: int

    async def close(self):
        await super().close()

        # I would like type validation and also the next closes to run.
        # Even if they don't exist or somehow are None?
        try:
            log.error("HERE")
            await self.mcws.close()
        except (AttributeError, TypeError):
            pass

        try:
            log.error("OR HERE")
            await self.mnws.close()
        except (AttributeError, TypeError):
            pass


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


@bot.check
async def is_owner(ctx: Context):
    return await ctx.bot.is_owner(ctx.author)


bot.run(getenv("TOKEN"))
