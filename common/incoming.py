# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import Literal, TypedDict

from .ws_opcode import Opcode

__all__ = (
    "Login",
    "LoginData",
    "Message",
    "MessageData",
    "IncomingMessage",
)


class Login(TypedDict):
    o: Literal[Opcode.LOGIN]
    d: LoginData


class LoginData(TypedDict):
    uuid: str
    v: str


class Message(TypedDict):
    o: Literal[Opcode.MESSAGE]
    d: MessageData


class MessageData(TypedDict):
    msg: str
    auth: str
    name: str


IncomingMessage = Login | Message
