import pytest
import logging

logging.basicConfig(level=logging.DEBUG)


@pytest.fixture(scope='session')
def fix():
    from datetime import datetime as t
    return "fix" + str(t.now())


@pytest.fixture(scope='session')
def think(fix):
    def _think(msg):
        return f"{fix} + {msg}";

    return _think
