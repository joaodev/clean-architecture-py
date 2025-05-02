from typing import Dict
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.domain.models.user import User

class UserFinder(UserFinderInterface):
    """
    Implementation of the UserFinder use case.
    """

    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        """
        Initialize the UserFinder use case.
        """

        self.__users_repository = users_repository


    def find(self, user_id: int) -> Dict:
        """
        Find a user by their ID.

        :param user_id: The ID of the user to find.
        :return: A dictionary containing user information.
        """

        user = self.__find_user_by_id(user_id)
        response = self.__format_response(user)
        return response

    def find_by_first_name(self, first_name: str) -> Dict:
        """
        Find a user by their First Name.

        :param first_name: The First Name of the user to find.
        :return: A dictionary containing user information.
        """

        user = self.__find_user_by_name(first_name)
        response = self.__format_response(user)
        return response


    @classmethod
    def __validate_first_name(cls, first_name: str) -> None:
        """
        Validate the first_name format.

        :param first_name: The first name to validate.
        :raises Exception: If the first name is not valid.
        """

        if not first_name:
            raise Exception("First name cannot be empty")
        if not first_name.isalpha():
            raise Exception("First name must contain only alphabetic characters")
        if len(first_name) < 2:
            raise Exception("First name must be at least 2 characters long")
        if len(first_name) > 50:
            raise Exception("First name must be at most 50 characters long")

    def __find_user_by_id(self, user_id: int) -> User:
        """
        Find a user by their ID.

        :param user_id: The ID of the user to find.
        :return: A dictionary containing user information.
        """

        if not user_id:
            raise Exception("User ID cannot be empty")

        user = self.__users_repository.get_user_by_id(user_id)
        if not user:
            raise Exception("User not found")
        return user

    def __find_user_by_name(self, first_name: str) -> User:
        """
        Find a user by their First Name.

        :param first_name: The First Name of the user to find.
        :return: A dictionary containing user information.
        """

        self.__validate_first_name(first_name)
        user = self.__users_repository.get_user_by_first_name(first_name)
        if not user:
            raise Exception("User not found")
        return user

    @classmethod
    def __format_response(cls, data: User) -> Dict:
        """
        Format the response.

        :param data: The data to format.
        :return: A dictionary containing the formatted response.
        """

        return {
            "data": data
        }
