# Copyright 2022-latest Oliver Wilkes. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with, the Elastic License 2.0
# https://www.elastic.co/licensing/elastic-license

from __future__ import annotations

from typing import TYPE_CHECKING

from botbase import CogBase

if TYPE_CHECKING:
    from minecat.__main__ import Minecat


class LinkServer(CogBase["Minecat"]):
    ...


def setup(bot: Minecat):
    bot.add_cog(LinkServer(bot))
