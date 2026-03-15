"""src — Anti-detection WhatsApp automation SDK."""

__version__ = "0.6"


from .BrowserManager import ProfileManager, ProfileInfo, Platform, CamoufoxBrowser, BrowserConfig
from .Encryption import MessageEncryptor, MessageDecryptor, KeyManager

__all__ = [
    "ProfileManager",
    "ProfileInfo",
    "Platform",
    "CamoufoxBrowser",
    "BrowserConfig",
    "MessageEncryptor",
    "MessageDecryptor",
    "KeyManager",
]
