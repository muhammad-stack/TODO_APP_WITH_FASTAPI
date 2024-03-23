# main.py
from contextlib import asynccontextmanager
from typing import Union, Optional, Annotated
from uit_fastapi import settings
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import FastAPI, Depends, HTTPException, Query


class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(index=True)


class Updated_Todo(SQLModel):
    content: Optional[str] = None


# only needed for psycopg 3 - replace postgresql
# with postgresql+psycopg in settings.DATABASE_URL
connection_string = str(settings.MAIN_DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)


# recycle connections after 5 minutes
# to correspond with the compute scale down
engine = create_engine(
    connection_string, connect_args={"sslmode": "require"}, pool_recycle=300
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# The first part of the function, before the yield, will
# be executed before the application starts.
# https://fastapi.tiangolo.com/advanced/events/#lifespan-function
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables..")
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan, title="Hello World API with DB",
              version="0.0.1",
              summary='A Todo with a POST DELETE PATCH GET FUNCTIONALITY FOR THE FRONTEND ',
              contact={
                  "name": "Syed Muhammad Ali Kazmi",
                  "url": "https://www.linkedin.com/in/syed-muhammad-ali-kazmi-b8a0732a0/",
                  "email": "nasi18994@gmail.com",
              },
              servers=[
                  {
                      "url": "http://0.0.0.0:8000",  # ADD NGROK URL Here Before Creating GPT Action
                      "description": "Development Server"
                  }
              ])


def get_session():
    with Session(engine) as session:
        yield session


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


session = Annotated[Session, Depends(get_session)]


@app.post("/todo", response_model=Todo)
def create_todo(todo: Todo, session: session):
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

# Offset = Starting Point of Retriving Data
# Limit = How much data to be fetched in a single request


@app.get("/todo", response_model=list[Todo])
def read_todos(session: session, offset: int = 0, limit: int = Query(default=50, le=50)):
    todos = session.exec(select(Todo).offset(offset).limit(limit)).all()
    return todos


@app.get('/todo/{todo_id}', response_model=Todo)
def get_todos(todo_id: int, session: session):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Not Found")
    return todo


@app.patch('/todo/{todo_id}', response_model=Updated_Todo)
def update_todo_byName(todo_id: int, session: session, todo: Updated_Todo):
    get_name = session.get(Todo, todo_id)
    if not get_name:
        raise HTTPException(status_code=404, detail="Not Found")
    new_data = todo.model_dump(exclude_unset=True)
    get_name.sqlmodel_update(new_data)
    session.add(get_name)
    session.commit()
    session.refresh(get_name)
    return get_name


@app.delete('/todo/{todo_id}')
def delete_hero_by_id(todo_id: int, session: session):
    content = session.get(Todo, todo_id)
    if not content:
        raise HTTPException(status_code=404, detail='ID NOT FOUND')
    session.delete(content)
    session.commit()
    return {"status": "deleted"}
