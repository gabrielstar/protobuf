import logging
import os
import types
from collections import namedtuple

import pytest
from keycloak import KeycloakOpenID
from .. import helpers

@pytest.fixture(scope='session')
def ctx():
    """
    We can for instance store tokens and revoke them at the end of test
    :return:
    """
    _ctx = types.SimpleNamespace()
    yield _ctx
    print(f"Context final state {_ctx}")
    print("Revoking any used tokens ...")


@pytest.fixture(scope='session')
def user():
    return helpers.User(os.environ.get('user'), os.environ.get('password'))


@pytest.fixture(scope='session')
def keycloak_config():
    return helpers.KeycloakConfig(os.environ.get('KEYCLOAK_URL'), os.environ.get("keycloak_client_id"),
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
