import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.resolve()))

from camouchat.BrowserManager.profile_manager import ProfileManager
from camouchat.BrowserManager.platform_manager import Platform

def test_profile_manager_manual():
    """Test full ProfileManager lifecycle: create, list, check existence, delete."""

    pm = ProfileManager()

    # Create two profiles (idempotent – OK if they already exist from a previous run)
    pm.create_profile(Platform.WHATSAPP, "test1")
    pm.create_profile(Platform.WHATSAPP, "test2")

    listing = pm.list_profiles(Platform.WHATSAPP)
    assert "whatsapp" in listing
    assert "test1" in listing["whatsapp"]
    assert "test2" in listing["whatsapp"]

    assert pm.is_profile_exists(Platform.WHATSAPP, "test1")
    assert pm.is_profile_exists(Platform.WHATSAPP, "test2")

    # Fetch profile info
    info = pm.get_profile(Platform.WHATSAPP, "test1")
    assert info.profile_id == "test1"

    # Delete both profiles
    pm.delete_profile(Platform.WHATSAPP, "test1", force=True)
    pm.delete_profile(Platform.WHATSAPP, "test2", force=True)

    assert not pm.is_profile_exists(Platform.WHATSAPP, "test1")
    assert not pm.is_profile_exists(Platform.WHATSAPP, "test2")
