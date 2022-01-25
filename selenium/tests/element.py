from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#this allows us to make elements as classes properties that can be read and assigned values like properties
class BasePageElement():

    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator)
        )
        driver.find_element(*self.locator).clear()
        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator)
        )
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")


# specific elements only need to provide locator
class SearchTextElement(BasePageElement):
    locator = (By.NAME, "q")

class GoButtonElement(BasePageElement):
    locator = (By.NAME, "go")
