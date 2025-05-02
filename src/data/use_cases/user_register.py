from typing import Dict
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.user_register import UserRegister as UserRegisterInterface

class UserRegister(UserRegisterInterface):
    """
    Implementation of the UserRegister use case.
    """

    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        """
        Initialize the UserRegister use case.
        """

        self.__users_repository = users_repository

    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        """
        Register a new user.

        :param value: The first name of the user.
        :param last_name: The last name of the user.
        :param age: The age of the user.
        :return: A dictionary containing the registered user's information.
        """

        self.__validate_value("First Name", first_name)
        self.__validate_value("Last Name", last_name)
        self.__validate_age(age)
        self.__register_user(first_name, last_name, age)

        response = self.__format_response(first_name, last_name, age)
        return response

    @classmethod
    def __validate_value(cls, field: str, value: str) -> None:
        """
        Validate the value format.

        :param field: The field to validate.
        :param value: The field value to validate.
        :raises Exception: If the first name is not valid.
        """

        if not value:
            raise Exception(f"{field} cannot be empty")
        if not value.isalpha():
            raise Exception(f"{field} must contain only alphabetic characters")
        if len(value) < 2:
            raise Exception(f"{field} must be at least 2 characters long")
        if len(value) > 50:
            raise Exception(f"{field} must be at most 50 characters long")

    @classmethod
    def __validate_age(cls, age: int) -> None:
        """
        Validate the age format.

        :param age: The age to validate.
        :raises Exception: If the age is not valid.
        """
        if not age:
            raise Exception("Age cannot be empty")
        if not isinstance(age, int):
            raise Exception("Age must be an integer")
        if age < 0:
            raise Exception("Age cannot be negative")

    def __register_user(self, first_name: str, last_name: str, age: int) -> None:
        """
        Register a new user in the repository.

        :param first_name: The first name of the user.
        :param last_name: The last name of the user.
        :param age: The age of the user.
        """
        return self.__users_repository.insert_user(first_name, last_name, age)

    @classmethod
    def __format_response(cls, first_name: str, last_name: str, age: int) -> Dict:
        """
        Format the response for the registered user.

        :param user: The user to format.
        :return: A dictionary containing the formatted user information.
        """
        return {
            "data": {
                "first_name": first_name,
                "last_name": last_name,
                "age": age
            }
        }
