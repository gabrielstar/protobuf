from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from locator import MainPageLocators, MenuLocators, FooterLocators
from abc import ABC, abstractmethod
from element import SearchTextElement, GoButtonElement
from settings import DriverSettings


class BasePage():
    def __init__(self, driver: webdriver):
        self.driver: webdriver = driver

    def find(self, by, value):
        WebDriverWait(self.driver, DriverSettings.MAX_WAIT.value).until(
            lambda driver: driver.find_element(by, value)
        )
        return self.driver.find_element(by, value)


class AbstractMenu():
    @abstractmethod
    def click_option(self, option):
        pass


class Menu(BasePage, AbstractMenu):
    def click_option(self, option):
        if option == "Python":
            self.find(*MenuLocators.PYTHON_MENU_BUTTON).click()
        else:
            raise ValueError("No such menu option")


class Footer(BasePage, AbstractMenu):
    def click_option(self, option):
        if option == "Python events":
            self.driver.find_element(*FooterLocators.EVENTS_PYTHON_EVENTS).click()
        else:
            raise ValueError("No such footer option")


class SkeletonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.menu = Menu(driver)
        self.footer = Footer(driver)


class MainPage(SkeletonPage):
    search_text_element = SearchTextElement()  # composition
    go_button_element = GoButtonElement()

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)  # it will unpack arguments By.ID, value ...
        element.click()


class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results found" not in self.driver.page_source
