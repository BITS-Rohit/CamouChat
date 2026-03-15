# 🏢 ProfileManager: The Boss of Your Profiles

The `ProfileManager` is the brain of your profile organization. It’s responsible for creating, fetching, listing, and even deleting profiles for any platform (like `Platform.WHATSAPP`).

Think of it as a **Warehouse Manager** who knows exactly where each profile's box is and what's inside.

---

### 🛠️ Getting Started

First, import it and create an instance:
```python
from camouchat.BrowserManager import ProfileManager
pm_obj = ProfileManager()
```

---

### 📦 Key Functions

#### 1. `create_profile(platform, profile_id)`
**Required Parameters:**
*   `platform` (`Platform`): Which platform is this for? e.g., `Platform.WHATSAPP`
*   `profile_id` (`str`): The name you want to give your profile (e.g., "Work").

If the profile doesn't exist, it **creates** it. If it already exists, it **returns** its existing data.
```python
profile = pm_obj.create_profile(Platform.WHATSAPP, "Work")
```

---

#### 2. `enable_encryption(platform, profile_id)`
**Required Parameters:**
*   `platform` (`Platform`)
*   `profile_id` (`str`)

This generates a **32-byte AES-256 key** for your profile. This key is NOT stored in the metadata—it's a secret file (`encryption.key`) that only you (and the code) can read.
- **Returns**: The raw bytes of the key.
```python
key = pm_obj.enable_encryption(Platform.WHATSAPP, "Work")
# Pass this key to MessageProcessor to encrypt your messages!
```

---

#### 3. `get_key(platform, profile_id)`
**Required Parameters:**
*   `platform`, `profile_id`

Loads the existing encryption key for a profile. Use this when resuming a session to keep your messages readable.

---

#### 4. `list_profiles(platform=None)`
**Optional Parameter:**
*   `platform` (`Platform`): If given, lists profiles for that platform only.

Lists all profiles you have currently saved on your computer. Great for showing a menu to the user!
```python
all_profiles = pm_obj.list_profiles()
print(f"I have these profiles: {all_profiles}")
```

---

#### 5. `delete_profile(platform, profile_id, force=False)`
**Required Parameters:**
*   `platform`, `profile_id`
**Optional Parameter:**
*   `force` (`bool`): If `True`, deletes even if the profile is currently active.

This **destroys** the profile from your disk. **Warning: This is permanent!** All messages and saved sessions will be gone.
```python
pm_obj.delete_profile(Platform.WHATSAPP, "Work")
```

---

### 🛡️ Why use the ProfileManager?
- **Isolation**: Each profile is sandboxed in its own directory. One profile's cookies or data will **never** leak into another.
- **Organization**: No need to worry about where files are on your disk; the Manager handles paths for you.
- **Encryption**: Built-in methods to secure your data with the push of a button.

---

### 💡 Pro Tip
The `ProfileManager` is designed to be very efficient. You can keep one instance of it running throughout your application to manage all your bots! 🤖
