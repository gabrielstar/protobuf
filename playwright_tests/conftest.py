import pytest
from playwright_tests.pages.result import DuckDuckGoResultPage
from playwright_tests.pages.search import DuckDuckGoSearchPage


@pytest.fixture
def result_page(page):
    return DuckDuckGoResultPage(page)


@pytest.fixture
def search_page(page):
    return DuckDuckGoSearchPage(page)
