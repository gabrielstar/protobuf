from typing import NamedTuple


class UserCredentials(NamedTuple):
    """Represents user credentials."""

    username: str
    password: str
