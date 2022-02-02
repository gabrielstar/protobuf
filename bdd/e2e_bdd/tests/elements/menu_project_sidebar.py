from playwright.sync_api import Locator

from bdd.e2e_bdd.tests.elements.base_element import BaseElement


class MenuProjectSidebar(BaseElement):
    PROJECTS_BUTTON = 'div.ms-Nav-linkText:has-text("Projects")'

    @property
    def projects_button(self) -> Locator:
        return self.page.locator(self.PROJECTS_BUTTON)
