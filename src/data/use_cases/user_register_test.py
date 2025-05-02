from src.infra.db.tests.users_repository_memory import UsersRepositoryMemory
from .user_register import UserRegister

def test_user_register():
    """
    Test the UserRegister use case.
    """

    users_repository = UsersRepositoryMemory()
    user_register = UserRegister(users_repository)

    response = user_register.register("John", "Doe", 30)

    assert response["data"]["first_name"] == "John"
    assert response["data"]["last_name"] == "Doe"
    assert response["data"]["age"] == 30

def test_user_register_invalid_first_name():
    """
    Test the UserRegister use case with an invalid first name.
    """

    users_repository = UsersRepositoryMemory()
    user_register = UserRegister(users_repository)

    try:
        user_register.register("", "Doe", 30)
    except Exception as e:
        assert str(e) == "First Name cannot be empty"

def test_user_register_invalid_last_name():
    """
    Test the UserRegister use case with an invalid last name.
    """

    users_repository = UsersRepositoryMemory()
    user_register = UserRegister(users_repository)

    try:
        user_register.register("John", "", 30)
    except Exception as e:
        assert str(e) == "Last Name cannot be empty"

def test_user_register_empty_age():
    """
    Test the UserRegister use case with an empty age format.
    """

    users_repository = UsersRepositoryMemory()
    user_register = UserRegister(users_repository)

    try:
        user_register.register("John", "Doe", "")
    except Exception as e:
        assert str(e) == "Age cannot be empty"


def test_user_register_invalid_age_format():
    """
    Test the UserRegister use case with an invalid age format.
    """

    users_repository = UsersRepositoryMemory()
    user_register = UserRegister(users_repository)

    try:
        user_register.register("John", "Doe", "thirty")
    except Exception as e:
        assert str(e) == "Age must be an integer"

def test_user_register_invalid_age():
    """
    Test the UserRegister use case with an invalid age.
    """

    users_repository = UsersRepositoryMemory()
    user_register = UserRegister(users_repository)

    try:
        user_register.register("John", "Doe", -1)
    except Exception as e:
        assert str(e) == "Age cannot be negative"

def test_user_register_too_short_first_name():
    """
    Test the UserRegister use case with a too short first name.
    """

    users_repository = UsersRepositoryMemory()
    user_register = UserRegister(users_repository)

    try:
        user_register.register("J", "Doe", 30)
    except Exception as e:
        assert str(e) == "First Name must be at least 2 characters long"

def test_user_register_too_long_first_name():
    """
    Test the UserRegister use case with a too long first name.
    """

    users_repository = UsersRepositoryMemory()
    user_register = UserRegister(users_repository)

    try:
        user_register.register("J" * 51, "Doe", 30)
    except Exception as e:
        assert str(e) == "First Name must be at most 50 characters long"

def test_user_register_too_short_last_name():
    """
    Test the UserRegister use case with a too short last name.
    """

    users_repository = UsersRepositoryMemory()
    user_register = UserRegister(users_repository)

    try:
        user_register.register("John", "D", 30)
    except Exception as e:
        assert str(e) == "Last Name must be at least 2 characters long"

def test_user_register_too_long_last_name():
    """
    Test the UserRegister use case with a too long last name.
    """

    users_repository = UsersRepositoryMemory()
    user_register = UserRegister(users_repository)

    try:
        user_register.register("John", "D" * 51, 30)
    except Exception as e:
        assert str(e) == "Last Name must be at most 50 characters long"

def test_user_register_invalid_first_name_format():
    """
    Test the UserRegister use case with an invalid first name format.
    """

    users_repository = UsersRepositoryMemory()
    user_register = UserRegister(users_repository)

    try:
        user_register.register("John123", "Doe", 30)
    except Exception as e:
        assert str(e) == "First Name must contain only alphabetic characters"

def test_user_register_invalid_last_name_format():
    """
    Test the UserRegister use case with an invalid last name format.
    """

    users_repository = UsersRepositoryMemory()
    user_register = UserRegister(users_repository)

    try:
        user_register.register("John", "Doe123", 30)
    except Exception as e:
        assert str(e) == "Last Name must contain only alphabetic characters"

def test_user_register_invalid_first_name_special_characters():
    """
    Test the UserRegister use case with an invalid first name format.
    """

    users_repository = UsersRepositoryMemory()
    user_register = UserRegister(users_repository)

    try:
        user_register.register("John@Doe", "Doe", 30)
    except Exception as e:
        assert str(e) == "First Name must contain only alphabetic characters"

def test_user_register_invalid_last_name_special_characters():
    """
    Test the UserRegister use case with an invalid last name format.
    """

    users_repository = UsersRepositoryMemory()
    user_register = UserRegister(users_repository)

    try:
        user_register.register("John", "Doe@Doe", 30)
    except Exception as e:
        assert str(e) == "Last Name must contain only alphabetic characters"

def test_user_register_invalid_first_name_numeric():
    """
    Test the UserRegister use case with an invalid first name format.
    """

    users_repository = UsersRepositoryMemory()
    user_register = UserRegister(users_repository)

    try:
        user_register.register("John123", "Doe", 30)
    except Exception as e:
        assert str(e) == "First Name must contain only alphabetic characters"

def test_user_register_invalid_last_name_numeric():
    """
    Test the UserRegister use case with an invalid last name format.
    """

    users_repository = UsersRepositoryMemory()
    user_register = UserRegister(users_repository)

    try:
        user_register.register("John", "Doe123", 30)
    except Exception as e:
        assert str(e) == "Last Name must contain only alphabetic characters"
