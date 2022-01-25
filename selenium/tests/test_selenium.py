from selenium import webdriver
import page


def test_search_python(driver, base_url):
    main_page = page.MainPage(driver)
    assert main_page.is_title_matches()
    main_page.search_text_element = "pycon"
    main_page.click_go_button()
    search_result_page = page.SearchResultPage(driver)
    assert search_result_page.is_results_found()
    main_page.menu.click_option("Python")
    main_page.footer.click_option("Python events")
    driver.implicitly_wait(3)
