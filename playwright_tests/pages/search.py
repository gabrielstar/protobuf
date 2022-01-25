# A page object class typically has three main parts:
#
# Selectors and any other data stored as variables
# Dependency injection of the browser automator through a constructor
# Interaction methods that use the browser automator and the selectors

class DuckDuckGoSearchPage:
    #class methods
    SEARCH_BUTTON = '#search_button_homepage'
    SEARCH_INPUT = '#search_form_input_homepage'
    URL = 'https://www.duckduckgo.com' #(Warning: Base URLs should typically be passed into automation code as an input, not hard-coded in a page object. We are doing this here as a matter of simplicity for this workshop.)

    def __init__(self, page): #in playwright_tests we inject page instead of a driver
        self.page = page

    def load(self):
        self.page.goto(self.URL)

    def search(self, phrase):
        self.page.fill(self.SEARCH_INPUT, phrase)
        self.page.click(self.SEARCH_BUTTON)