from src.infra.db.repositories.users_repository import UsersRepository
from .user_finder import UserFinder

def test_user_finder():
    """
    Test the UserFinder use case.
    """
    users_repository = UsersRepository()
    user_finder = UserFinder(users_repository)
