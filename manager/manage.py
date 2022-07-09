from asyncio import new_event_loop

from mineager import run


loop = new_event_loop()
loop.create_task(run())


try:
    loop.run_forever()
finally:
    loop.close()
