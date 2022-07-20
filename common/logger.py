# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from logging import getLogger, Formatter, INFO
from logging.handlers import TimedRotatingFileHandler
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logging import Logger


__all__ = ("ws_logger_factory",)


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
