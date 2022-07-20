# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from logging import Formatter, LoggerAdapter, getLogger, INFO
from logging.handlers import TimedRotatingFileHandler
from common import ws_logger_factory

__all__ = ("default_logger",)


class UUIDAdapter(LoggerAdapter):
    def process(self, msg, kwargs):
        try:
            websocket = kwargs["extra"]["websocket"]
        except KeyError:
            return msg, kwargs

        xff = websocket.request_headers.get("CF-Connecting-IP")
        uuid = getattr(websocket, "uuid", "unknown".ljust(22))
        return f"{uuid} {xff}: {msg}", kwargs


raw_default_logger = ws_logger_factory(logger_name="mineager.websocket", directory="mg")
default_logger = UUIDAdapter(raw_default_logger)
