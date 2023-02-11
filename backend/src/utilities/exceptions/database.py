class EntityDoesNotExist(Exception):
    """
    Throw an exception when the dentity does not exist in the database.
    """


class EntityAlreadyExists(Exception):
    """
    Throw an exception when the entity already exists in the database.
    """


class UsernameAlreadyExists(Exception):
    """
    Throw an exception when the username already registered.
    """


class EmailAlreadyExists(Exception):
    """
    Throw an exception when the email already registered.
    """


class PasswordDoesNotMatch(Exception):
    """
    Throw an error if Account password doesn't match.
    """
