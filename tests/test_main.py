from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session
from uit_fastapi.fastapi import app, get_session
from uit_fastapi import settings


def test_read_main():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_write_main():
    connection_string = str(settings.TEST_DATABASE_URL).replace(
        "postgresql", "postgresql+psycopg")
    engine = create_engine(
        connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:

        def get_session_override():
            return session
        app.dependency_overrides[get_session] = get_session_override

        client = TestClient(app)

        todo_content = "buy bread"
        response = client.post("/todo/",
                               json={"content": todo_content}
                               )
        app.dependency_overrides.clear()
        data = response.json()
        assert response.status_code == 200
        assert data["content"] == todo_content


def test_read_list_main():

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

        response = client.get("/todos/")
        assert response.status_code == 200
