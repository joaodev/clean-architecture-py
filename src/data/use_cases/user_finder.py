from typing import Dict
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface

class UserFinder(UserFinderInterface):
    """
    Implementation of the UserFinder use case.
    """

    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        """
        Initialize the UserFinder use case.
        """
        self.__users_repository = users_repository


    def find(self, user_id: str) -> Dict:
        """
        Find a user by their ID.

        :param user_id: The ID of the user to find.
        :return: A dictionary containing user information.
        """

        response = self.__users_repository.get_user_by_id(user_id)
        return response
