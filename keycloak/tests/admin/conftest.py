import logging
import os
import types
from collections import namedtuple

import pytest
from keycloak import KeycloakOpenID, KeycloakAdmin
from .. import helpers

@pytest.fixture(scope='session')
def admin():
    return helpers.User(os.environ.get('admin_user'), os.environ.get('admin_password'))


@pytest.fixture(scope='session')
def keycloak_admin_config():
    return helpers.KeycloakConfig(os.environ.get('KEYCLOAK_URL'), os.environ.get("admin_client_id"),
                          os.environ.get('admin_realm_name'))


@pytest.fixture(scope='session')
def keycloak_admin_client(keycloak_admin_config, admin) -> KeycloakAdmin:
    logging.info(f"Getting keycloak client")

    keycloak_admin = KeycloakAdmin(server_url=keycloak_admin_config.url,
                               username=admin.user,
                               password=admin.password,
                               realm_name=keycloak_admin_config.realm_name,
                               client_id=keycloak_admin_config.client_id,
                               client_secret_key=None,
                               verify=False)

    yield keycloak_admin

    logging.info("\nDestroying Keycloak client")
    del keycloak_admin
