# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from orjson import dumps
from websockets.server import WebSocketServerProtocol

from .ws_opcode import Opcode

if TYPE_CHECKING:
    from typing import Any, Coroutine, Generic, TypeVar

    from manager.websocket import State as ManagerState
    from minecat.websocket import State as BotState

    from .outgoing import OutgoingMessage

    T = TypeVar("T")
    StateT = TypeVar("StateT", bound=ManagerState | BotState)
    Coro = Coroutine[Any, Any, T]


__all__ = ("Websocket",)
log = getLogger(__name__)


class Websocket(WebSocketServerProtocol, Generic[StateT]):
    def __init__(self, state: StateT, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.state = state

    def send_login(self, *, uuid: str | None) -> Coro[None]:
        return self.send_json(
            {
                "o": Opcode.LOGIN,
                "d": {"uuid": uuid},
            }
        )

    def send_json(self, data: OutgoingMessage) -> Coro[None]:
        return self.send(dumps(data))
