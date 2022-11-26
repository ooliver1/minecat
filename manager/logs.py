# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license


from logging import INFO, Formatter, StreamHandler, getLogger
from logging.handlers import RotatingFileHandler

__all__ = ("set_logging",)


def set_logging():
    formatter = Formatter(
        "%(levelname)-7s %(asctime)s %(filename)12s:%(funcName)-28s: %(message)s",
        datefmt="%H:%M:%S %d/%m/%Y",
    )
    h = RotatingFileHandler(
        "./logs/manager/io.log",
        maxBytes=1000000,
        backupCount=5,
        encoding="utf-8",
    )
    i = StreamHandler()

    i.setFormatter(formatter)
    h.setFormatter(formatter)
    h.namer = lambda name: name.replace(".log", "") + ".log"
    root = getLogger()
    root.setLevel(INFO)
    root.addHandler(i)
    root.addHandler(h)
