"""All the Humanized Operation Interface modules"""

from abc import ABC, abstractmethod
from typing import Optional, Union

from playwright.async_api import Page
from logging import Logger, LoggerAdapter
from camouchat.camouchat_logger import camouchatLogger

from camouchat.Interfaces.web_ui_selector import WebUISelectorCapable


class HumanInteractionControllerInterface(ABC):
    """
    All Humanized Altered Operation here.
    """

    @abstractmethod
    def __init__(
        self,
        page: Page,
        log: Optional[Union[Logger, LoggerAdapter]],
        UIConfig: WebUISelectorCapable,
        **kwargs,
    ) -> None:
        self.page = page
        self.log = log or camouchatLogger
        self.UIConfig = UIConfig

    @abstractmethod
    async def typing(self, text: str, **kwargs) -> bool: ...
