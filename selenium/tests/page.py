from selenium import webdriver
from locator import MainPageLocators

from element import SearchTextElement, GoButtonElement


class BasePage():
    def __init__(self, driver: webdriver):
        self.driver: webdriver = driver


class MainPage(BasePage):
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
