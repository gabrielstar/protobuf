from logging import Logger

import pytest
from playwright.sync_api import Page

from bdd.e2e_bdd.tests.pages.login import LoginPage
from bdd.e2e_bdd.tests.pages.projects_grid import ProjectsGridPage
from pytest_bdd import given, then, parsers
import time


@pytest.fixture
def login_page(page: Page, logger: Logger) -> LoginPage:
    return LoginPage(page, logger)


@pytest.fixture
def projects_grid_page(page: Page, logger: Logger) -> ProjectsGridPage:
    return ProjectsGridPage(page, logger)


# shared BDD steps
@given("Login page is displayed")
def login_page_is_displayed(login_page):
    login_page.navigate()


@given("I log in")
def i_log_in(login_page, user):
    login_page.do_login(*user)


@then(parsers.parse("I wait for {seconds:d} seconds"))
def i_wait_for_seconds(seconds):
    time.sleep(seconds)
    assert True
