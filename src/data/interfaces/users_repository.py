from abc import ABC, abstractmethod

from src.domain.models.user import User

class UsersRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        """
        Insert a new user into the database.
        """

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        """
        Retrieve a user by their ID.
        """

    @abstractmethod
    def get_user_by_first_name(self, first_name: str) -> User:
        """
        Retrieve a user by their First Name.
        """
