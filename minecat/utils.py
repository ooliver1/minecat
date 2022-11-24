# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from os import environ as env

from docker import Client as DockerClient
from nextcord import Intents, MemberCacheFlags

INTENTS = Intents(guilds=True, guild_messages=True, members=True, message_content=True)
MEMBER_CACHE_FLAGS = MemberCacheFlags.none()


docker = DockerClient(base_url="unix://var/run/docker.sock")
HOSTNAME = env["HOSTNAME"]
all_containers = docker.containers()
our_container = [c for c in all_containers if c["Id"][:12] == HOSTNAME[:12]][0]
current_cluster = our_container["Labels"]["com.docker.compose.container-number"]

TOTAL_CLUSTERS = int(env["TOTAL_CLUSTERS"])
TOTAL_SHARDS = int(env["TOTAL_SHARDS"])
SHARD_COUNT = TOTAL_SHARDS // TOTAL_CLUSTERS
SHARD_IDS = list(
    range(
        SHARD_COUNT * (int(current_cluster) - 1),
        SHARD_COUNT * (int(current_cluster)),
    )
)
