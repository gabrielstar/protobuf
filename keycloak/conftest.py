import logging
import os
from collections import namedtuple

import pytest
from keycloak import KeycloakOpenID

logging.basicConfig(level=logging.INFO)
User = namedtuple("User", ["user", "password"])
KeycloakConfig = namedtuple("KeycloakConfig", ["url", "client_id", "realm_name"])


@pytest.fixture(scope='session')
def user():
    return User(os.environ.get('user'), os.environ.get('password'))


@pytest.fixture(scope='session')
def keycloak_config():
    return KeycloakConfig(os.environ.get('KEYCLOAK_URL'), os.environ.get("keycloak_client_id"),
                          os.environ.get('keycloak_realm_name'))


@pytest.fixture(scope='session')
def keycloak_client(keycloak_config) -> KeycloakOpenID:
    logging.info(f"Getting keycloak client")

    keycloak_openid = KeycloakOpenID(server_url=keycloak_config.url,
                                     client_id=keycloak_config.client_id,
                                     realm_name=keycloak_config.realm_name)
    yield keycloak_openid

    logging.info("\nDestroying Keycloak client")
    del keycloak_openid
