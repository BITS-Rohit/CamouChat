from abc import ABC, abstractmethod
from typing import Optional, Union

from playwright.async_api import ElementHandle, Locator


class ChatInterface(ABC):
    """Chat Interface Base Class"""

    chat_name: str
    chat_id: str
    chat_ui: Optional[Union[Locator, ElementHandle]]
    System_Hit_Time: float

    @abstractmethod
    def _chat_key(self, **kwargs) -> str:
        """Calculate unique chat key."""
        ...
