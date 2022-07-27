# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from logging import INFO, Formatter, LoggerAdapter, getLogger
from logging.handlers import TimedRotatingFileHandler
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from logging import Logger


__all__ = ("ws_logger_factory", "UUIDAdapter")


def ws_logger_factory(*, logger_name: str, directory: str) -> Logger:
    logger = getLogger(logger_name)
    logger.setLevel(INFO)
    h = TimedRotatingFileHandler(f"./logs/{directory}/io.log", when="midnight")
    h.setFormatter(
        Formatter(
            "%(levelname)-7s %(asctime)s %(filename)12s:%(funcName)-28s: %(message)s",
            datefmt="%H:%M:%S %d/%m/%Y",
        )
    )
    h.namer = lambda name: name.replace(".log", "") + ".log"
    logger.addHandler(h)
    return logger


class UUIDAdapter(LoggerAdapter[Logger]):
    def process(self, msg: str, kwargs: Any):
        try:
            websocket = kwargs["extra"]["websocket"]
        except KeyError:
            return msg, kwargs

        xff = websocket.request_headers.get("CF-Connecting-IP")
        uuid = getattr(websocket, "uuid", "unknown".ljust(22))
        return f"{uuid} {xff}: {msg}", kwargs
