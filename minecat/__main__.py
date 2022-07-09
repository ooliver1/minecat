# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import TYPE_CHECKING
from asyncio import set_event_loop_policy
from os import getenv

from mineager import run
from botbase import BotBase
from dotenv import load_dotenv
from nextcord import Intents
from uvloop import EventLoopPolicy

if TYPE_CHECKING:
    from websockets.server import WebSocketServer

set_event_loop_policy(EventLoopPolicy())
load_dotenv()


class MyBot(BotBase):
    mcws: WebSocketServer

    async def startup(self, *args, **kwargs):
        self.mcws = await run()

        await super().startup(*args, **kwargs)


intents = Intents.none()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
bot = MyBot(intents=intents)


bot.run(getenv("TOKEN"))
