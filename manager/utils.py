from __future__ import annotations

import time
from asyncio import Future
from asyncio.events import get_event_loop
from logging import getLogger
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from asyncio.events import AbstractEventLoop


log = getLogger(__name__)
__all__ = ("Limiter",)


class Limiter:
    def __init__(
        self,
        limit: int,
        per: float,
        *,
        identifier: str,
        loop: AbstractEventLoop | None = None,
    ) -> None:
        self.limit = limit
        self.per = per
        self.identifier = identifier

        self.current = self.limit
        self._reserved: list[Future] = []
        self.loop: AbstractEventLoop = loop or get_event_loop()
        self.pending_reset = False

    async def __aenter__(self) -> Limiter:
        while True:
            if self.current == 0:
                log.info("Ratelimiting limiter %s", self.identifier)
                future = self.loop.create_future()
                self._reserved.append(future)
                await future
            else:
                break

        self.current -= 1

        if not self.pending_reset:
            self.pending_reset = True
            self.loop.call_later(self.per, self.reset)

        return self

    async def __aexit__(self, *_) -> None:
        ...

    def reset(self) -> None:
        log.info("Resetting limiter %s", self.identifier)
        current_time = time.time()
        self.reset_at = current_time + self.per
        self.current = self.limit

        for _ in range(self.limit):
            try:
                self._reserved.pop().set_result(None)
            except IndexError:
                break

        if len(self._reserved):
            self.pending_reset = True
            self.loop.call_later(self.per, self.reset)
        else:
            self.pending_reset = False
