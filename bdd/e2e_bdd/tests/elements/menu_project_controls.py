from playwright.sync_api import Locator

from bdd.e2e_bdd.tests.elements.base_element import BaseElement


class MenuProjectControls(BaseElement):
    NEW_PROJECT_BUTTON = 'span.ms-Button-label:has-text("New Project")'
    GRID_BUTTON = 'span.ms-Button-label:has-text("Grid")'
    LIST_BUTTON = 'span.ms-Button-label:has-text("List")'

    @property
    def new_project_button(self) -> Locator:
        return self.page.locator(self.NEW_PROJECT_BUTTON)

    @property
    def grid_button(self) -> Locator:
        return self.page.locator(self.GRID_BUTTON)

    @property
    def list_button(self) -> Locator:
        return self.page.locator(self.LIST_BUTTON)

    def click_all_controls(self):
        controls = [self.list_button, self.grid_button, self.new_project_button]
        for control in controls:
            control.click()
            self.page.press("body", "Escape")
