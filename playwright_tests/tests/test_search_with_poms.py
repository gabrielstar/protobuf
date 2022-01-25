import pytest

PHRASES = [
    "duck",
    "goose",
    "elephant",
    "tiger"
]

@pytest.mark.parametrize('phrase', PHRASES)
def test_basic_duckduckgo_search(search_page, result_page, phrase):
    search_page.load()
    search_page.search(phrase)
    assert phrase == result_page.search_input_value()
    assert result_page.result_link_titles_contain_phrase(phrase)
    assert phrase in result_page.title()
