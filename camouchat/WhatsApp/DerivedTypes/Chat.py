"""
WhatsApp Chat contracted with ChatInterface Template
"""

from __future__ import annotations
import time
from dataclasses import dataclass, field
from typing import Optional, Union

from playwright.async_api import ElementHandle, Locator


from camouchat.Interfaces.chat_interface import ChatInterface


@dataclass
class whatsapp_chat(ChatInterface):
    chat_name: str
    chat_ui: Optional[Union[ElementHandle, Locator]]
    chat_id: str = field(init=False)
    System_Hit_Time: float = field(default_factory=time.time)

    def __post_init__(self):
        self.chat_id = self._chat_key()

    def _chat_key(self, **kwargs) -> str:
        return f"wa::{self.chat_name.lower().strip()}"
