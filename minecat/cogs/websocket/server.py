# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from logging import INFO, Formatter, LoggerAdapter, getLogger
from logging.handlers import TimedRotatingFileHandler
from typing import TYPE_CHECKING

from botbase import CogBase
from orjson import loads
from websockets.server import serve

from ._server import WebSocketServer

if TYPE_CHECKING:
    from asyncio import Future

    from minecat.__main__ import Minecat


class UUIDAdapter(LoggerAdapter):
    def process(self, msg, kwargs):
        try:
            websocket = kwargs["extra"]["websocket"]
        except KeyError:
            return msg, kwargs

        xff = websocket.request_headers.get("CF-Connecting-IP")
        uuid = getattr(websocket, "uuid", "unknown".ljust(22))
        return f"{uuid} {xff}: {msg}", kwargs


raw_logger = getLogger("mineager.websocket")
raw_logger.setLevel(INFO)
h = TimedRotatingFileHandler("./logs/ws/io.log", when="midnight")
h.setFormatter(
    Formatter(
        "%(levelname)-7s %(asctime)s %(filename)12s:%(funcName)-28s: %(message)s",
        datefmt="%H:%M:%S %d/%m/%Y",
    )
)
h.namer = lambda name: name.replace(".log", "") + ".log"
raw_logger.addHandler(h)
logger = UUIDAdapter(raw_logger)


class Server(CogBase["Minecat"]):
    def __init__(self, bot: Minecat) -> None:
        super().__init__(bot)
        self.future: Future[None] = bot.loop.create_future()
        bot.loop.create_task(self.start_ws())

    def cog_unload(self) -> None:
        self.future.set_result(None)

    async def start_ws(self) -> None:
        async with serve(
            self.handler,  # type: ignore
            # I would like my own custom class here.
            # It also includes the req path, as type checkers do not like union callables.
            # Why does websockets include typings for deprecated features? I do not know.
            create_protocol=WebSocketServer,  # type: ignore
            # websockets' typing here is dumb, it has only one param which is false
            logger=logger,
            port=int(f"69{str(self.bot.cluster).rjust(2, '0')}"),
            # the port is `69{cluster}`, rjust is to add leading 0s to the cluster id
        ) as ws:
            self.bot.mcws = ws
            await self.future

    async def handler(self, ws: WebSocketServer) -> None:
        ws.logger.debug("< Received new connection")
        async for message in ws:
            await self.bot.manager(ws=ws, data=loads(message))


def setup(bot: Minecat):
    bot.add_cog(Server(bot))