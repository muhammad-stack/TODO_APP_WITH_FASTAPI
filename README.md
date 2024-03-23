<h1>FastAPI Project<h1>
This is a project that uses FastAPI, a modern, fast, and easy-to-use web framework for building APIs with Python.

<h1>What is FastAPI?<h1>
FastAPI is a web framework that is based on standard Python type hints and ASGI (Asynchronous Server Gateway Interface). It has several features that make it ideal for building APIs, such as:

Fast: It has very high performance, comparable to Node.js and Go, thanks to Starlette and Pydantic.
Easy: It is designed to be easy to learn and use, with intuitive and expressive syntax, and great editor support.
Robust: It generates automatic interactive documentation for your API, based on OpenAPI and JSON Schema standards. It also supports dependency injection, authentication, validation, testing, and more.
Scalable: It supports asynchronous code, concurrency, and websockets, allowing you to build scalable and real-time applications.
You can learn more about FastAPI from its official website or its GitHub repository.

<h1>How to install FastAPI using Poetry?<h1>
Poetry is a tool that helps you manage your Python projects and dependencies. It allows you to create virtual environments, specify your dependencies, and publish your packages to PyPI. You can install Poetry by following the official instructions.

To create a FastAPI project using Poetry, you can follow these steps:

<li>Create a new project with poetry new fastapi-project.<li>
<li>Add FastAPI and Uvicorn (an ASGI server) as dependencies with poetry add fastapi uvicorn[standard].<li>
<li>Activate the virtual environment with poetry shell.<li>
<li>Create a file named app.py in the project folder, and write your FastAPI code there. For example:<li>

`
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
return {"message": "Hello, world!"}

`

<li>Run the server with uvicorn app:app --reload.<li>

<h1>How to use GET method and path parameters and query parameters?<h1>
The GET method is one of the HTTP methods that you can use to define your API endpoints. It is used to retrieve data from the server, without modifying it. You can use the @app.get decorator to create a GET endpoint in FastAPI.

Path parameters are variables that are part of the URL path. They are used to identify a specific resource or resources. You can use the @app.get("/{parameter}") syntax to define a path parameter, and use the same name as a function argument to access its value. For example:
`@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}`
This endpoint will return the item with the given id, such as {"item_id": 42} for http://localhost:8000/items/42.

Query parameters are key-value pairs that are appended to the URL after a question mark (?). They are used to sort, filter, or paginate the data. You can use the @app.get decorator with optional function arguments to define query parameters. For example:
`@app.get("/users")
def get_users(name: str = None, age: int = None, limit: int = 10):
    users = get_all_users()
    if name:
        users = filter_by_name(users, name)
    if age:
        users = filter_by_age(users, age)
    users = users[:limit]
    return {"users": users}
`
This endpoint will return a list of users, optionally filtered by name and age, and limited by the limit parameter. For example, http://localhost:8000/users?name=alice&age=25&limit=5 will return the first five users with the name Alice and the age 25.
