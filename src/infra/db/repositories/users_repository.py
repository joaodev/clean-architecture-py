from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity

class UsersRepository:

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
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

    @classmethod
    def get_user_by_id(cls, user_id: int) -> UsersEntity:
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

    @classmethod
    def get_user_by_first_name(cls, first_name: str) -> UsersEntity:
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
