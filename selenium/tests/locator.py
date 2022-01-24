from selenium.webdriver.common.by import By


class MainPageLocators():
    GO_BUTTON = (By.ID, "submit")  # (how,value)
    SEARCH_TEXT_ELEMENT = (By.NAME, "q")


class SearchResultsPageLocators():
    pass
