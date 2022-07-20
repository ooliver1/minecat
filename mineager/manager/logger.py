# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from common import ws_logger_factory

__all__ = ("default_logger",)


default_logger = ws_logger_factory(logger_name="mineager.manager", directory="mn")
