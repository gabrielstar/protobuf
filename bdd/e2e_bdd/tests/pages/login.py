from __future__ import annotations

from typing import List
from playwright.sync_api import TimeoutError
from bdd.e2e_bdd.tests.pages.base import BasePage
from bdd.e2e_bdd.tests.utils import constants


class LoginPage(BasePage):
    PATH: str = "/"
    LOGIN_BUTTON: str = "text=Log In"
    LICENSE_AGREEMENT_BUTTONS: List[str] = [
        '//button[contains(@title, "I agree")]'
        '/span/span/span[contains(text(), "agree")]'
    ]
    USERNAME_INPUT: str = 'input[name="username"]'
    PASSWORD_INPUT: str = 'input[name="password"]'
    LOGIN_BUTTON_SUBMIT: str = 'input[name="login"]'

    def click_login(self) -> LoginPage:
        self.page.locator(self.LOGIN_BUTTON).click()
        return self

    def agree_to_license(self) -> LoginPage:
        try:
            self.page.click(
                *self.LICENSE_AGREEMENT_BUTTONS, timeout=constants.SELECTOR_MEDIUM_WAIT
            )
        except TimeoutError:
            self.logger.info(
                "Looks like no licence agreement dialog displayed, that's OK"
            )

        return self

    def enter_user_details(self, username: str, password: str) -> LoginPage:
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        return self

    def submit_login_form(self) -> LoginPage:
        self.page.click(self.LOGIN_BUTTON_SUBMIT)
        return self

    def do_login(self, username: str, password: str) -> None:
        self.click_login().agree_to_license().enter_user_details(
            username, password
        ).submit_login_form()
