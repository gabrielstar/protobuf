from selenium.webdriver.common.by import By


class MainPageLocators():
    GO_BUTTON = (By.ID, "submit")  # (how,value)
    SEARCH_TEXT_ELEMENT = (By.NAME, "q")


class MenuLocators():
    PYTHON_MENU_BUTTON = (By.XPATH, '//*[@id="top"]/nav/ul/li[1]/a')


class FooterLocators():
    EVENTS_PYTHON_EVENTS = (By.LINK_TEXT, "Python Events")


class SearchResultsPageLocators():
    pass
