#running with `pytest tests` will not add current dir to PYTHON_PATH, running `python -m pytest tests` will do it
#so any code referenced from outside of test dir will work

def test_basic_duckduckgo_search(page):
    # Given the DuckDuckGo home page is displayed
    page.goto("https://www.duckduckgo.com", wait_until='load')
    # When the user searches for a phrase
    page.fill('#search_form_input_homepage', 'panda') #playwright_tests waits for these elements to be editable
    page.click('#search_button_homepage') #to be clickable
    # Then the search result query is the phrase
    assert 'panda' == page.input_value("#search_form_input") #playwright_tests waits for element to be ready
    # And the search result links pertain to the phrase
    page.locator(".result__title a.result__a >> nth=4").wait_for()
    titles = page.locator('.result__title a.result__a ').all_text_contents()
    #panda_titles =  list(filter(lambda title: 'panda' in title.lower(), titles))
    panda_titles = [t for t in titles if 'panda' in t.lower()]
    assert len(panda_titles) > 0
    # And the search result title contains the phrase
    assert 'panda' in page.title()