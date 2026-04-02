"""
Works on new Wa-js Based API scripts.

Wraps the CHAT API's data into a dataclass
"""

from dataclasses import dataclass
from typing import Any

@dataclass
class ChatModelAPI:
    """
    Keys : 
    id_serialized : It is JID of the whatsapp. 
    unreadCount : Shows how many unreadCount this chat has.
    """
    id_serialized: str
    unreadCount: int | None = 0
    isAutoMuted: bool | None = False
    timestamp: int | None = 0
    isArchived: bool | None = False
    isLocked: bool | None = False
    isNotSpam: bool | None = True
    disappearingModeTrigger: str | None = None
    disappearingModeInitiator: str | None = None
    unreadMentionCount: int | None = 0
    lastChatEntryTimestamp: int | None = 0
    isOpened: bool | None = False
    isReadOnly: bool | None = False
    isTrusted: bool | None = True
    formattedTitle: str | None = None
    groupSafetyChecked: bool | None = False
    canSend: bool | None = True
    proxyName: str | None = "chat"
    isCommunity: bool | None = False

    @classmethod
    def from_dict(cls, data: dict) -> "ChatModelAPI":
        """
        Creates a ChatModelAPI from the raw dictionary returned by WA-JS.
        Handles the '__x_' prefixes automatically.
        """
        def get_val(key: str, default: Any = None):
            return data.get(key, data.get(f"__x_{key}", default))

        is_parent = get_val("isParentGroup", False)
        group_type = get_val("groupType", "DEFAULT")
        is_comm = (is_parent is True) | (group_type == "ANNOUNCEMENT")

        return cls(
            id_serialized=get_val("id_serialized") or data.get("id", {}).get("_serialized") or None,
            unreadCount=get_val("unreadCount") or None,
            isAutoMuted=get_val("isAutoMuted") or None,
            timestamp=get_val("t") or get_val("timestamp") or None,
            isArchived=get_val("archive") or None,
            isLocked=get_val("isLocked") or None,
            isNotSpam=get_val("notSpam") or None,
            disappearingModeTrigger=get_val("disappearingModeTrigger") or None,
            disappearingModeInitiator=get_val("disappearingModeInitiator") or None,
            unreadMentionCount=get_val("unreadMentionCount") or None,
            lastChatEntryTimestamp=get_val("lastChatEntryTimestamp") or None,
            isOpened=get_val("hasOpened") or None,
            isReadOnly=get_val("isReadOnly") or None,
            isTrusted=get_val("trusted") or None,
            formattedTitle=get_val("formattedTitle") or get_val("name") or None,
            groupSafetyChecked=get_val("groupSafetyChecked") or None,
            canSend=get_val("canSend") or None,
            proxyName=get_val("proxyName") or None,
            isCommunity=is_comm
        )

