# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from logging import INFO, Formatter, LoggerAdapter, getLogger
from logging.handlers import TimedRotatingFileHandler


__all__ = ("logger",)


class UUIDAdapter(LoggerAdapter):
    def process(self, msg, kwargs):
        try:
            websocket = kwargs["extra"]["websocket"]
        except KeyError:
            return msg, kwargs

        xff = websocket.request_headers.get("CF-Connecting-IP")
        uuid = getattr(websocket, "uuid", "unknown".ljust(22))
        return f"{uuid} {xff}: {msg}", kwargs


raw_logger = getLogger("minecat.cogs.websocket")
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
raw_logger.propagate = False
logger = UUIDAdapter(raw_logger)
