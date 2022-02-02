import os
import types
import logging

import pytest

from bdd.e2e_bdd.tests.helpers.model import UserCredentials

logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope="session")
def logger() -> logging.Logger:
    return logging.getLogger("bdd-e2e-tests")


@pytest.fixture(scope="session")
def hac_username():
    return os.environ["HAC_USERNAME"]


@pytest.fixture(scope="session")
def hac_password():
    return os.environ["HAC_PASSWORD"]


@pytest.fixture(scope="session")
def app_instance_url(pytestconfig):
    opt = pytestconfig.getoption("--base-url")
    if opt:
        return opt
    return os.environ["APP_INSTANCE_URL"]


@pytest.fixture(scope="session")
def user(hac_username: str, hac_password: str) -> UserCredentials:
    return UserCredentials(hac_username, hac_password)


@pytest.fixture(scope="session")
def web_session(user, app_instance_url) -> types.SimpleNamespace:
    _session = types.SimpleNamespace()
    _session.user = user
    return _session
