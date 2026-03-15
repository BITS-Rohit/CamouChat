# 🔐 Login: Your Gateway to WhatsApp

The `Login` class handles the authentication flow to get your profile connected to WhatsApp Web. Once you log in, your session is automatically saved to your `ProfileInfo`'s cache directory!

Like all core components, it uses a **Singleton-per-Page Pattern**, meaning it protects you from accidentally running multiple login scripts on the same connected browser page.

---

### 🛠️ Setting up the Login

To initialize the `Login` handler, you need the same three components you use across the SDK: your `page`, your `UIConfig`, and your `logger`.

```python
from camouchat.WhatsApp import Login, WebSelectorConfig

# Make sure you have your UI Config ready!
ui_config_obj = WebSelectorConfig(page=page_obj, log=camouchatLogger)

login_obj = Login(
    page=page_obj,
    # ------------- Required Parameter -------------
    # The active browser page instance. We support Asyncio only.

    UIConfig=ui_config_obj,
    # ------------- Required Parameter -------------
    # Pass the UI Config object here so we know how to interact with the DOM.

    log=camouchatLogger
    # ------------- Required Parameter -------------
    # Used for logging errors and the pairing code!
)
```

# --- Let's get logged in! ---

### 📦 Key Functions

#### 1. `login(**kwargs)`
This is the main function that handles both **QR Code Scanning** and **Phone Number Linking (Code-based)**.

```python
# Here is how you do a Code-Based Login:

success = await login_obj.login(
    method=1,
    # ------------- Required Parameter -------------
    # 0 FOR QR BASED LOGIN.
    # 1 FOR CODE BASED LOGIN.
    # Note: It is only a 1-time setup for your profile; afterward, it will auto-save the session.
    
    number=1234567890,
    # ------------- Required Parameter (If method=1) -------------
    # No need to add the country code, just the local number.
    
    country="India",
    # ------------- Required Parameter (If method=1) -------------
    # The SDK will automatically type and select your country from the dropdown.
    
    wait_time=150_000,
    # ------------- Optional Parameter -------------
    # The time it waits for QR scan or Code to be processed. Defaults to 180_000 (180s).
    
    url="https://web.whatsapp.com"
    # ------------- Optional Parameter -------------
    # Optional URL if you need to override the default.
)

if success:
    print("Woohoo! We are logged in!")
```

> **A note on Code Based Login (method=1)**: 
> If you choose to log in with your phone number, the SDK will print an 8-character code in your terminal. WhatsApp will send a notification to your phone. Tap it, and enter the code into your mobile app!

---

#### 2. `is_login_successful(**kwargs)`
Checks if the login was actually successful by waiting for the Chat List to become visible on the screen.

```python
is_connected = await login_obj.is_login_successful(
    timeout=10_000
    # ------------- Optional Parameter -------------
    # How long to wait for the UI to load (default: 10_000 ms).
)
```

---

### 🚪 What about Logging Out?

The `Login` class does **NOT** have a `.logout()` method!

Since your sessions are isolated into `ProfileManager` sandboxes, there are two ways to securely log out:

1.  **Delete the Profile**: Just delete the profile using `ProfileManager`. This wipes all cache, media, and session data entirely.
    ```python
    pm_obj.delete_profile(Platform.WHATSAPP, "Work")
    ```
2.  **Via the Mobile App**: Go to WhatsApp on your phone -> **Linked Devices** -> tap on the device -> **Log Out**. Next time your bot runs, it will simply ask to log in again!
