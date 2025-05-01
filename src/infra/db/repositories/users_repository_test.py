import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from .users_repository import UsersRepository

db_connection = DBConnectionHandler()
connection = db_connection.get_engine().connect()

@pytest.mark.skip(reason="Skipping test_insert_user for now")
def test_insert_user():
    user = {
        "first_name": "Lorem",
        "last_name": "Ipsum",
        "age": 31,
    }

    users_repository = UsersRepository()
    users_repository.insert_user(user["first_name"], user["last_name"], user["age"])

    sql = '''
        SELECT * FROM users WHERE first_name = '{}' AND last_name = '{}' AND age = {}
    '''.format(
        user["first_name"],
        user["last_name"],
        user["age"]
    )

    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.first_name == user["first_name"]
    assert registry.last_name == user["last_name"]
    assert registry.age == user["age"]
    assert registry.id is not None
    assert registry.id > 0

    connection.execute(text(f"DELETE FROM users WHERE id = {registry.id}"))
    connection.commit()

@pytest.mark.skip(reason="Skipping test_select_user for now")
def test_get_user_by_id():
    user = {
        "first_name": "Lorem",
        "last_name": "Ipsum",
        "age": 31,
    }

    users_repository = UsersRepository()
    users_repository.insert_user(user["first_name"], user["last_name"], user["age"])

    sql = '''
        SELECT * FROM users WHERE first_name = '{}' AND last_name = '{}' AND age = {}
    '''.format(
        user["first_name"],
        user["last_name"],
        user["age"]
    )

    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    user_id = registry.id

    response = users_repository.get_user_by_id(user_id)

    assert response.first_name == user["first_name"]
    assert response.last_name == user["last_name"]
    assert response.age == user["age"]
    assert response.id == user_id

    connection.execute(text(f"DELETE FROM users WHERE id = {registry.id}"))
    connection.commit()

@pytest.mark.skip(reason="Skipping test_select_user for now")
def test_select_user():
    user = {
        "first_name": "Lorem",
        "last_name": "Ipsum",
        "age": 31,
    }

    users_repository = UsersRepository()
    users_repository.insert_user(user["first_name"], user["last_name"], user["age"])

    response = users_repository.get_user_by_first_name(user["first_name"])

    assert response.first_name == user["first_name"]
    assert response.last_name == user["last_name"]
    assert response.age == user["age"]
    assert response.id is not None
    assert response.id > 0

    connection.execute(text(f"DELETE FROM users WHERE id = {response.id}"))
    connection.commit()
