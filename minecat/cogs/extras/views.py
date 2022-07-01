from __future__ import annotations

from typing import TYPE_CHECKING

from nextcord.ui import Button, View

if TYPE_CHECKING:
    from nextcord import Emoji, PartialEmoji


class LinkButtonView(View):
    def __init__(
        self, name: str, url: str, emoji: str | PartialEmoji | Emoji | None = None
    ):
        super().__init__()
        if emoji is not None:
            self.add_item(Button(label=name, url=url, emoji=emoji))
        else:
            self.add_item(Button(label=name, url=url))
