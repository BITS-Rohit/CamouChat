from abc import ABC, abstractmethod
from typing import Optional, Union

from playwright.async_api import ElementHandle, Locator

from camouchat.Interfaces.chat_interface import ChatInterface


class MessageInterface(ABC):
    """Message Interface Base Class"""

    system_hit_time: float
    raw_data: str
    data_type: Optional[str]
    parent_chat: ChatInterface
    message_ui: Optional[Union[ElementHandle, Locator]]
    message_id: Optional[str]

    @abstractmethod
    def _message_key(self) -> str:
        """Calculate unique message key."""
        ...
