import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.skip("simple example")
def test_is_title_exist(driver, base_url):
    driver.get(base_url)
    print(driver.title)
    assert driver.title


@pytest.mark.skip("simple example")
def test_search_with_wait(driver, base_url, settings):
    driver.get(base_url)
    search = driver.find_element_by_name("s")
    search.clear()
    search.send_keys("test")
    search.send_keys(Keys.ENTER)
    try:
        main = WebDriverWait(driver, settings.SHORT_WAIT).until(
            EC.presence_of_element_located((By.ID, "main"))
        )
        articles = main.find_elements_by_tagname("article")
        for article in articles:
            header = article.find_element_by_class_name("entry-summary")
            print(header.text)

    except:
        driver.close()


@pytest.mark.skip("simple example")
def test_navigation_back_forth(driver, base_url, settings):
    driver.get(base_url)
    link = driver.find_element_by_link_text("Python Programming")
    link.click()
    link = WebDriverWait(driver, settings.SHORT_WAIT).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    link.click()
    driver.back()
    driver.back()
    driver.forward()

@pytest.mark.skip("simple example")
def test_action_chains(driver, base_url, settings):
    driver.get(base_url)
    driver.implicitly_wait(settings.LONG_WAIT)
    cookie = driver.find_element_by_id("bigCookie")
    cookie_count = driver.find_element_by_id("cookies")
    items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

    actions = ActionChains(driver)
    for _ in range(50):
        print('clicking')
        actions.click(cookie)
        count = int(cookie_count.text.split(" ")[0])
        for item in items:
            value = int(item.text)
            if value <= count:
                upgrade_actions =  ActionChains(driver)
                upgrade_actions.move_to_element(items)
                upgrade_actions.click()
                upgrade_actions.perform()

    actions.perform()
    WebDriverWait(driver, settings.SHORT_WAIT)
