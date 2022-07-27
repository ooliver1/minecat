# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, TypedDict

from .opcode import Opcode

if TYPE_CHECKING:
    ...


class LoginData(TypedDict):
    o: Literal[Opcode.LOGIN]
    d: int


class LinkedData(TypedDict):
    o: Literal[Opcode.LINKED]
    d: str


class RestartData(TypedDict):
    o: Literal[Opcode.RESTART]
    d: int


class FindData(TypedDict):
    o: Literal[Opcode.FIND]
    d: FindInnerData


class FindInnerData(TypedDict):
    nonce: int
    uuid: str
    guild: int


ManagerJsonType = LoginData | LinkedData | RestartData | FindData
