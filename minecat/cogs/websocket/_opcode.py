# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from enum import IntEnum

__all__ = ("Opcode",)
class Opcode(IntEnum):
    LOGIN = 0
    MESSAGE = 1
    ERROR = 2
