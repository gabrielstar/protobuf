from __future__ import annotations

import logging

from playwright.sync_api import Page

from bdd.e2e_bdd.tests.elements.menu_project_controls import MenuProjectControls
from bdd.e2e_bdd.tests.elements.menu_project_sidebar import MenuProjectSidebar
from bdd.e2e_bdd.tests.pages.base import BasePage


class ProjectsListPage(BasePage):
    PATH: str = "/#projects/list"

    def __init__(self, page: Page, logger: logging.Logger):
        super().__init__(page, logger)
        self.menu_project_controls = MenuProjectControls(page)
        self.menu_project_sidebar = MenuProjectSidebar(page)
