# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from asyncio import get_event_loop
from asyncio import run as async_run
from signal import SIGTERM

from mineager import run


async def main():
    loop = get_event_loop()

    stop = loop.create_future()
    loop.add_signal_handler(SIGTERM, stop.set_result, None)

    ws_server, manager_server = run()

    async with ws_server, manager_server:
        await stop


async_run(main())
