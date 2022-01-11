def test_add_user(keycloak_admin_client):
    # Add user
    new_user = keycloak_admin_client.create_user({"email": "example@example.com",
                                                  "username": "example@example.com",
                                                  "enabled": True,
                                                  "firstName": "Example",
                                                  "lastName": "Example"})
    print(f"Created/Fetched new user with ID of  {new_user}")
    response = keycloak_admin_client.delete_user(user_id=new_user)
    print(f"Deleted user of id {new_user} with status ")
