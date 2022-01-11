from keycloak import KeycloakAdmin

url = "http://localhost:10001/auth/"
client_id = "test_client"
realm_name = "master"
client_secret_key = None
username = "admin"
password = "admin"

keycloak_admin = KeycloakAdmin(server_url=url,
                               username=username,
                               password=password,
                               realm_name="master",
                               client_id="admin-cli",
                               client_secret_key=None,
                               verify=False)

# Add user
new_user = keycloak_admin.create_user({"email": "example@example.com",
                                       "username": "example@example.com",
                                       "enabled": True,
                                       "firstName": "Example",
                                       "lastName": "Example"})
print(f"Created/Fetched new user with ID of  {new_user}")

response = keycloak_admin.delete_user(user_id=new_user)
print(f"Deleted user of id {new_user} with status ")
