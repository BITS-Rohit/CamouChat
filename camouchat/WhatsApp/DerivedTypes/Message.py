"""WhatsApp Message Class contracted with Message Interface Template"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Union, Literal, Optional

from playwright.async_api import ElementHandle, Locator

from camouchat.WhatsApp.DerivedTypes.Chat import whatsapp_chat


from camouchat.Interfaces.message_interface import MessageInterface


@dataclass
class whatsapp_message(MessageInterface):
    """Should inherit the protocol from Message Interface Template"""

    direction: Literal["in", "out"]
    data_id: str

    raw_data: str
    parent_chat: whatsapp_chat
    message_ui: Optional[Union[ElementHandle, Locator]]

    data_type: Optional[str] = None
    message_id: str = field(init=False)
    system_hit_time: float = field(default_factory=time.time)

    # Message body encryption (set by MessageProcessor when encryption is enabled)
    encrypted_message: Optional[str] = None
    encryption_nonce: Optional[str] = None

    # Chat name encryption (set by MessageProcessor when encryption is enabled)
    # encrypted_chat_name / chat_name_nonce: AES-256-GCM ciphertext of the real chat name
    # parent_chat_name_index: HMAC-SHA256 hex digest used as the queryable DB index value
    encrypted_chat_name: Optional[str] = None
    chat_name_nonce: Optional[str] = None
    parent_chat_name_index: Optional[str] = None  # replaces plaintext in DB when encrypted

    def isIncoming(self) -> Optional[bool]:
        """
        Specifies the direction of message.
        returns : True if incoming else False
        """
        if self.direction == "in":
            return True
        if self.direction == "out":
            return False
        return None

    def __post_init__(self):
        self.message_id = self._message_key()

    def _message_key(self) -> str:
        return f"wa-msg::{self.data_id}"
