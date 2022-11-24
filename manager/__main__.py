# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from asyncio import Event, gather, new_event_loop, run, set_event_loop
from typing import TYPE_CHECKING

from .client import Manager

if TYPE_CHECKING:
    from typing import Literal


async def main(*, manager: Manager, event: Event) -> tuple[None, Literal[True]]:
    return await gather(manager.start(), event.wait())


if __name__ == "__main__":
    event = Event()
    manager = Manager(event=event)

    loop = new_event_loop()
    set_event_loop(loop)

    try:
        run(main(manager=manager, event=event))
    except KeyboardInterrupt:
        pass
    finally:
        loop.run_until_complete(manager.close())
        loop.close()
