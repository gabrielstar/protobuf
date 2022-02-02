from playwright.sync_api import Page


class BaseElement:
    def __init__(self, page: Page):
        self.page = page
