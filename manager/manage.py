from asyncio import get_event_loop
from asyncio import run as async_run
from signal import SIGTERM

from mineager import run


async def main():
    loop = get_event_loop()

    stop = loop.create_future()
    loop.add_signal_handler(SIGTERM, stop.set_result, None)

    async with run():
        await stop


async_run(main())
