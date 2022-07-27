# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import TYPE_CHECKING

from .opcode import Opcode
from .storage import storage

if TYPE_CHECKING:
    from .protocol import ClusteredWebSocketServer


async def handle(ws: ClusteredWebSocketServer) -> None:
    async for message in ws:
        message["o"] = Opcode(message["o"])  # type: ignore
        # Assign the actual Opcode without messing about with the protocol.
        # Gets some fancy Union table types \o/

        if message["o"] == Opcode.LOGIN:
            cluster = message["d"]
            if not isinstance(cluster, int):
                ws.logger.error(
                    "Opcode.LOGIN's data payload must be an int, not %s", type(cluster)
                )
                continue

            storage[cluster] = ws
            ws.cluster = cluster
        elif message["o"] == Opcode.RESTART:
            cluster = message["d"]
            if not isinstance(cluster, int):
                ws.logger.error(
                    "Opcode.RESTART's data payload must be an int, not %s",
                    type(cluster),
                )
                continue

            if cluster == -1:
                for ws in storage.values():
                    await storage[cluster].send({"o": Opcode.RESTART})

            if cluster not in storage:
                ws.logger.error("Cluster %d not found", cluster)
                ws.logger.info("Clusters found %s", storage)
                continue

            await storage[cluster].send({"o": Opcode.RESTART})

    # I would like type validation
    try:
        storage.pop(ws.cluster, None)
    except AttributeError:
        pass
