from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.user import User

class UsersRepository(UsersRepositoryInterface):

    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        """
        Insert a new user into the database.
        """
        with DBConnectionHandler() as db:
            try:
                user = UsersEntity(first_name=first_name, last_name=last_name, age=age)
                db.session.add(user)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
            finally:
                db.session.close()

    def get_user_by_id(self, user_id: int) -> User:
        """
        Retrieve a user by their ID.
        """
        with DBConnectionHandler() as db:
            try:
                user = (
                    db.session.query(UsersEntity)
                    .filter(UsersEntity.id == user_id)
                    .first()
                )
                return user
            except Exception as e:
                db.session.rollback()
                raise e
            finally:
                db.session.close()

    def get_user_by_first_name(self, first_name: str) -> User:
        """
        Retrieve a user by their First Name.
        """
        with DBConnectionHandler() as db:
            try:
                user = (
                    db.session.query(UsersEntity)
                    .filter(UsersEntity.first_name == first_name)
                    .first()
                )
                return user
            except Exception as e:
                db.session.rollback()
                raise e
            finally:
                db.session.close()
