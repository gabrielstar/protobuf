import types
from typing import NamedTuple

import pytest
import logging
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
    # return "https://techwithtim.net"
    return "https://orteil.dashnet.org/cookieclicker"


@pytest.fixture(scope='session')
def driver_path():
    return "/Users/gs/PycharmProjects/protobuf/selenium/driver/chromedriver"


@pytest.fixture(scope='session')
def driver(driver_path):
    driver = webdriver.Chrome(driver_path)
    yield driver
    driver.quit()
