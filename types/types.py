from playwright.sync_api import Page


class BasePage:
    def __init__(self):
        self.page: Page = ""


class NewPage(BasePage):
    pass


n = NewPage()

print(type(n))
print(isinstance(n, (BasePage, NewPage)))

print(hasattr(n, "page"))
attr = getattr(n, "page")
print(type(attr))
