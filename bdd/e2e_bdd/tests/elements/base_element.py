from logging import Logger

from playwright.sync_api import Page


class BaseElement:
    def __init__(self, page: Page, logger: Logger):
        self.page = page
        self.logger = logger
