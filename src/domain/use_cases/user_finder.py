from abc import ABC, abstractmethod
from typing import Dict

class UserFinder(ABC):
    """
    Abstract base class for user finder use cases.
    """

    @abstractmethod
    def find(self, user_id: str) -> Dict:
        """
        Find a user by their ID.

        :param user_id: The ID of the user to find.
        :return: A dictionary containing user information.
        """
