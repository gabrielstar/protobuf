from __future__ import annotations

import logging

from playwright.sync_api import Page

from bdd.e2e_bdd.tests.elements.menu_project_controls import MenuProjectControls
from bdd.e2e_bdd.tests.elements.menu_project_sidebar import MenuProjectSidebar
from bdd.e2e_bdd.tests.pages.base import BasePage


class ProjectsGridPage(BasePage):
    PATH: str = "/#projects/grid"

    def __init__(self, page: Page, logger: logging.Logger) -> None:
        super().__init__(page, logger)
        self.menu_project_controls = MenuProjectControls(page, logger)
        self.menu_project_sidebar = MenuProjectSidebar(page, logger)

    def click_projects_controls(self):
        self.menu_project_controls.click_all_controls()

    def open_projects(self):
        self.menu_project_sidebar.projects_button.click()

    def click_menus(self):
        self.click_projects_controls()
        self.open_projects()
