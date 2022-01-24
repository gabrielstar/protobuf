import logging
import types
from pathlib import Path
import pytest
from selenium import webdriver

logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope='session')
def settings():
    settings = types.SimpleNamespace()
    settings.SHORT_WAIT = 0.5
    settings.LONG_WAIT = 4
    return settings


@pytest.fixture(scope='session')
def base_url():
    return "https://python.org"


@pytest.fixture(scope='session')
def driver_path():
    return Path().resolve().parent.joinpath("driver/chromedriver")


@pytest.fixture(scope='session')
def driver(driver_path, base_url):
    driver = webdriver.Chrome(driver_path)
    driver.get(base_url)
    yield driver
    driver.quit()
