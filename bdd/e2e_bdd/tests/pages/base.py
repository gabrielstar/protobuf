import logging
from playwright.sync_api import Page


class BasePage:
    PATH: str = ""

    def __init__(self, page: Page, logger: logging.Logger):
        self.page = page
        self.logger = logger

    def navigate(self) -> None:
        self.page.goto(self.PATH)

    def is_at_page(self) -> bool:
        return self.PATH in self.page.url

    def title(self) -> str:
        return self.page.title()

    def escape(self):
        self.page.press("body", "Escape")
