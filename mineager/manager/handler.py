# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from websockets.server import WebSocketServerProtocol


async def handle(ws: WebSocketServerProtocol):
    async for message in ws:
        print(message)
