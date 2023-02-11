def http_400_bad_request_details() -> str:
    return f"Bad request!"


def http_400_username_details(username: str) -> str:
    return f"The username {username} is taken! Be creative and choose another one!"


def http_400_email_details(email: str) -> str:
    return f"The email {email} is already registered! Be creative and choose another one!"


def http_400_signup_credentials_details() -> str:
    return "Signup failed! Recheck all your credentials!"


def http_400_sigin_credentials_details() -> str:
    return "Signin failed! Recheck all your credentials!"


def http_401_unauthorized_details() -> str:
    return "Refused to complete request due to lack of valid authentication!"


def http_403_forbidden_details() -> str:
    return "Refused access to the requested resource!"


def http_404_id_details(id: int) -> str:
    return f"Either the entity with id `{id}` doesn't exist or has been deleted!"


def http_404_username_details(username: str) -> str:
    return f"Either the account with username `{username}` doesn't exist or has been deleted!"


def http_404_email_details(email: str) -> str:
    return f"Either the account with email `{email}` doesn't exist or has been deleted!"


def http_404_name_details(name: str) -> str:
    return f"Either the entity with name {name} doesn't exist or has been deleted!"
