# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from os import getenv
from minecat import __version__


db_url = getenv("DB_URI")
version = __version__
logchannel = getenv("LOG_CHANNEL")
