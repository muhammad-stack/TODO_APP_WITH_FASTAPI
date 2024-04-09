from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session
from uit_fastapi.fastapi import app, get_session, Todo
from uit_fastapi import settings


# def test_read_main():
#     client = TestClient(app=app)
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"msg": "Hello World"}


# def test_write_main():
#     connection_string = str(settings.TEST_DA TABASE_URL).replace(
#         "postgresql", "postgresql+psycopg")
#     engine = create_engine(
#         connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

#     SQLModel.metadata.create_all(engine)
#     with Session(engine) as session:

#         def get_session_override():
#             return session

#         app.dependency_overrides[get_session] = get_session_override

#         client = TestClient(app=app)

#         todo_content = "first"
#         response = client.post("/todo/",
#                                json={"content": todo_content}
#                                )
#         app.dependency_overrides.clear()
#         data = response.json()
#         assert response.status_code == 200
#         assert data["content"] == todo_content


# def test_read_list_main():

#     connection_string = str(settings.TEST_DATABASE_URL).replace(
#         "postgresql", "postgresql+psycopg")

#     engine = create_engine(
#         connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

#     SQLModel.metadata.create_all(engine)

#     with Session(engine) as session:

#         def get_session_override():
#             return session

#         app.dependency_overrides[get_session] = get_session_override
#         client = TestClient(app=app)

#         response = client.get("/todo/")
#         assert response.status_code == 200


# def test_get_todo_id():
#     connection_string = str(settings.TEST_DATABASE_URL).replace(
#         "postgresql", "postgresql+psycopg")

#     engine = create_engine(
#         connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

#     SQLModel.metadata.create_all(engine)

#     with Session(engine) as session:

#         def get_session_override():
#             return session

#         app.dependency_overrides[get_session] = get_session_override
#         client = TestClient(app=app)
#         todo_id: int = 20
#         response = client.get(f'/todo/{todo_id}')
#         app.dependency_overrides.clear()
#         assert response.status_code == 200


# def test_update_todo():
#     connection_string = str(settings.TEST_DATABASE_URL).replace(
#         "postgresql", "postgresql+psycopg")
#     engine = create_engine(
#         connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

#     SQLModel.metadata.create_all(engine)

#     with Session(engine) as session:

#         def get_session_override():
#             return session

#         app.dependency_overrides[get_session] = get_session_override

#         new_todo = Todo(content="Initial Content")
#         session.add(new_todo)
#         session.commit()

#         # Define the content to update

#         updated_content = "updated content"
#         client = TestClient(app=app)

#         response = client.patch(
#             f'/todo/{new_todo.id}', json={"content": updated_content})
#         app.dependency_overrides.clear()

#         data = response.json()
#         assert response.status_code == 200
#         assert data["content"] == updated_content


# def test_delete_todo():
#     connection_string = str(settings.TEST_DATABASE_URL).replace(
#         "postgresql", "postgresql+psycopg")
#     engine = create_engine(
#         connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

#     SQLModel.metadata.create_all(engine)

#     with Session(engine) as session:

#         def get_session_override():
#             return session

#         app.dependency_overrides[get_session] = get_session_override
#         client = TestClient(app=app)
#         todo_id: int = 26
#         response = client.delete(f'/todo/{todo_id}')
#         app.dependency_overrides.clear()
#         data = response.json()
#         assert response.status_code == 200

#         assert data == {"status": "deleted"}


def test_delete_all_todos():
    connection_string = str(settings.TEST_DATABASE_URL).replace(
        "postgresql", "postgresql+psycopg")
    engine = create_engine(
        connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        def get_session_override():
            return session
        app.dependency_overrides[get_session] = get_session_override
        client = TestClient(app=app)
        response = client.delete('/todo/')
        app.dependency_overrides.clear()
        data = response.json()
        assert response.status_code == 200
        assert data ==  {"message":"No content Found"}