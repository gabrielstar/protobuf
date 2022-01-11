def test_config_well_know(keycloak_client):
    """
    Assert we obtain configuration successfully
    :param keycloak_client:
    :return:
    """
    config_well_know = keycloak_client.well_know()
    assert config_well_know is not None


def test_token_creation(keycloak_client, user):
    """
    GIVEN client and user credentials
    WHEN token is created
    THEN access_token is returned
    :param keycloak_client:
    :param user:
    :return:
    """
    # Get Token
    token = keycloak_client.token(*user, totp="012345")
    token = keycloak_client.refresh_token(token['refresh_token'])
    assert token['access_token']
