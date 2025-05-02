from src.domain.models.user import User
from src.infra.db.tests.users_repository_memory import UsersRepositoryMemory
from .user_finder import UserFinder

def test_user_finder():
    """
    Test the UserFinder use case.
    """
    users_repository = UsersRepositoryMemory()
    user_finder = UserFinder(users_repository)

    response = user_finder.find(1)

    assert response is not None
    assert isinstance(response, dict)
    assert "data" in response
    assert isinstance(response["data"], User)

def test_user_finder_by_first_name():
    """
    Test the UserFinder use case by First Name.
    """
    users_repository = UsersRepositoryMemory()
    user_finder = UserFinder(users_repository)

    response = user_finder.find_by_first_name("Lorem")

    assert response is not None
    assert isinstance(response, dict)
    assert "data" in response
    assert isinstance(response["data"], User)

def test_find_error_user_not_found():
    """
    Test the UserFinder use case by ID with error.
    """
    class MockUsersRepository(UsersRepositoryMemory):
        def get_user_by_id(self, user_id: int) -> None:
            print(f"Finding user for tests: {user_id}")

    users_repository = MockUsersRepository()
    user_finder = UserFinder(users_repository)
    try:
        user_finder.find(999)
        assert False
    except Exception as e:
        assert str(e) == "User not found"

def test_find_error_in_id_empty():
    """
    Test the UserFinder use case by ID with error.
    """
    users_repository = UsersRepositoryMemory()
    user_finder = UserFinder(users_repository)

    try:
        user_finder.find("")
        assert False
    except Exception as e:
        assert str(e) == "User ID cannot be empty"

def test_find_error_in_first_name():
    """
    Test the UserFinder use case by First Name with error.
    """
    users_repository = UsersRepositoryMemory()
    user_finder = UserFinder(users_repository)

    try:
        user_finder.find_by_first_name("LoremIpsum123")
        assert False
    except Exception as e:
        assert str(e) == "First name must contain only alphabetic characters"

def test_find_error_in_first_name_empty():
    """
    Test the UserFinder use case by First Name with error.
    """
    users_repository = UsersRepositoryMemory()
    user_finder = UserFinder(users_repository)

    try:
        user_finder.find_by_first_name("")
        assert False
    except Exception as e:
        assert str(e) == "First name cannot be empty"

def test_find_error_in_first_name_too_short():
    """
    Test the UserFinder use case by First Name with error.
    """
    users_repository = UsersRepositoryMemory()
    user_finder = UserFinder(users_repository)

    try:
        user_finder.find_by_first_name("L")
        assert False
    except Exception as e:
        assert str(e) == "First name must be at least 2 characters long"

def test_find_error_in_first_name_too_long():
    """
    Test the UserFinder use case by First Name with error.
    """
    users_repository = UsersRepositoryMemory()
    user_finder = UserFinder(users_repository)

    try:
        user_finder.find_by_first_name("L" * 51)
        assert False
    except Exception as e:
        assert str(e) == "First name must be at most 50 characters long"
