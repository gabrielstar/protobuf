import logging
from collections import namedtuple

logging.basicConfig(level=logging.INFO)
User = namedtuple("User", ["user", "password"])
KeycloakConfig = namedtuple("KeycloakConfig", ["url", "client_id", "realm_name","client_secret"])
