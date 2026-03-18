"""Abstract base class for login handlers."""

from logging import Logger, LoggerAdapter
from typing import Optional, Union

from camouchat.camouchat_logger import camouchatLogger
from abc import ABC, abstractmethod

from playwright.async_api import Page

from camouchat.Interfaces.web_ui_selector import WebUISelectorCapable


class LoginInterface(ABC):
    """Base interface for authentication handlers."""

    def __init__(
        self,
        page: Page,
        UIConfig: WebUISelectorCapable,
        log: Optional[Union[Logger, LoggerAdapter]] = None,
    ):
        self.page = page
        self.UIConfig = UIConfig
        self.log = log or camouchatLogger

    @abstractmethod
    async def login(self, **kwargs) -> bool:
        """Perform login authentication."""
        ...

    @abstractmethod
    async def is_login_successful(self, **kwargs) -> bool:
        """Check if login was successful."""
        ...
