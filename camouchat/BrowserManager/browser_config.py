from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Dict, Optional

from camouchat.BrowserManager.platform_manager import Platform
from camouchat.Interfaces.browserforge_capable_interface import BrowserForgeCapable


@dataclass
class BrowserConfig:
    """
    Config dataclass for browser.
    """
    platform: Platform
    locale: str
    enable_cache: bool
    headless: bool
    fingerprint_obj: BrowserForgeCapable
    prefs: Optional[Dict[str, bool]] = None
    addons: List[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict) -> BrowserConfig:
        """dict should expose exact same name in the above given params."""
        return cls(
            platform=data["platform"],
            locale=data["locale"] or "en-US",
            enable_cache=data["enable_cache"] or False,
            headless=data["headless"] or False,
            prefs=data["prefs"] or {},
            addons=data["addons"] or [],
            fingerprint_obj=data["fingerprint_obj"],
        )
