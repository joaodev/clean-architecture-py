from src.domain.models.user import User


class UsersRepositoryMemory:

    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}


    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_attributes = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age
        }
        print(f"User inserted: {first_name} {last_name}, Age: {age}")

    def get_user_by_id(self, user_id: int) -> User:
        self.select_user_attributes = {user_id: user_id}
        print(f"User selected by ID: {user_id}")

        return User(
            id=user_id,
            first_name="Lorem",
            last_name="Ipsum",
            age=30
        )

    def get_user_by_first_name(self, first_name: str) -> User:
        self.select_user_attributes = {first_name: first_name}
        print(f"User selected by First Name: {first_name}")

        return User(
            id=1,
            first_name=first_name,
            last_name="Ipsum",
            age=30
        )
