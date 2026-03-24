import logging
from typing import Any, Callable, Dict, Optional

from playwright.async_api import Page
from .wajs_scripts import WAJS_Scripts

logger = logging.getLogger(__name__)


class WAJSError(Exception):
    """Exception raised when wa-js execution fails structurally or within React."""
    pass


class WapiWrapper:
    """
    The Bridge connecting Playwright (Python execution space) to wa-js (Browser space).
    Parses and handles the stealth-wrapped JSON responses from WAJS_Scripts.
    """

    def __init__(self, page: Page):
        self.page = page

    async def _evaluate_stealth(self, js_string: str) -> Any:
        """
        Executes a Stealth JS script in the browser.
        Handles the extraction of our standard `{status: '...', data|message: '...'}` format.
        """
        response = await self.page.evaluate(js_string)

        if not response or not isinstance(response, dict):
            raise WAJSError(f"Invalid stealth response format from browser: {response}")

        if response.get("status") == "error":
            # JS successfully swallowed a crash. We now raise it gracefully in Python.
            err_msg = response.get("message", "Unknown JavaScript Error in wa-js execution")
            logger.error(f"WA-JS Execution Error: {err_msg}")
            raise WAJSError(err_msg)

        return response.get("data")

    # --- 1. SETUP & CORE ---
    async def wait_for_ready(self, timeout_ms: float = 30000) -> bool:
        """Wait until `wa-js` completes Webpack hijack and exposes WPP"""
        logger.info("Awaiting WPP.isReady flag...")
        try:
            await self.page.wait_for_function(WAJS_Scripts.is_ready(), timeout=timeout_ms)
            logger.info("WPP successfully integrated and ready.")
            return True
        except Exception as e:
            logger.error("wa-js failed to initialize before timeout.")
            raise WAJSError("WPP Initialization Timeout") from e

    async def is_authenticated(self) -> bool:
        return await self._evaluate_stealth(WAJS_Scripts.is_authenticated())

    # --- 2. THE PUSH ARCHITECTURE (EVENTS) ---
    async def expose_message_listener(self, python_callback: Callable):
        """
        Exposes a Python handler to the browser to actively listen to WPP events.
        Zero-polling architecture.
        """
        alias = "__camou_message_proxy"
        
        # 1. Bind Python's callback to the browser's global JS space
        await self.page.expose_function(alias, python_callback)
        
        # 2. Tell WPP to start routing real-time WS payloads into our exposed function
        setup_script = WAJS_Scripts.setup_new_message_listener(alias)
        await self.page.evaluate(setup_script)
        logger.info(f"Stealth Message Push Listener activated via {alias}")

    # --- 3. DATA & ACTIONS ---
    async def get_chat(self, chat_id: str) -> Dict[str, Any]:
        return await self._evaluate_stealth(WAJS_Scripts.get_chat(chat_id))

    async def get_messages(self, chat_id: str, count: int = 50) -> list:
        return await self._evaluate_stealth(WAJS_Scripts.get_messages(chat_id, count))

    async def send_text_message(self, chat_id: str, message: str) -> Any:
        return await self._evaluate_stealth(
            WAJS_Scripts.send_text_message(chat_id, message)
        )
