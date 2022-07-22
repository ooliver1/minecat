# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from enum import IntEnum

__all__ = ("ServerError",)


class ServerError(IntEnum):
    MISSING_OPCODE = 0
    """The opcode field ("o") is missing."""
    UNKNOWN_OPCODE = 1
    """The opcode provided does not exist."""
