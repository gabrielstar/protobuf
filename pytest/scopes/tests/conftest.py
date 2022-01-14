import pytest


@pytest.fixture(scope='session')
def fix():
    from datetime import datetime as t
    return "_fix" + str(t.now())