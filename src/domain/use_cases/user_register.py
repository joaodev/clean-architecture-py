from abc import ABC, abstractmethod
from typing import Dict

class UserRegister(ABC):
    """
    Abstract base class for user registration use cases.
    """

    @abstractmethod
    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        """
        Register a new user.

        :param user_data: A dictionary containing user information.
        :return: A dictionary containing the registered user's information.
        """
