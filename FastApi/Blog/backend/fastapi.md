# Introduction to FastAPI

Setting up your development environment
• Creating a new FastAPI project
• Understanding FastAPI basics
• Defining your first API endpoint
• Working with path and query parameters
• Defining and using request and response models
• Handling errors and exceptions

## Technical Requirements

**Python**: FastAPI is built on Python, so you’ll need a Python version compatible with your FastAPI version. You can download the latest version of it from python.org.
**FastAPI**: Install FastAPI using pip, Python’s package manager. You can do it by running pip install fastapi from the command terminal.
**Uvicorn**: FastAPI requires an Asynchronous Server Gateway Interface (ASGI) server, and
Uvicorn is a lightning-fast ASGI server implementation.
**Integrated development environment (IDE)**: An IDE such as Visual Studio Code (VS Code), PyCharm, or any other IDE that supports Python development will be necessary for writing and testing your code.
**Postman or Swagger UI**: For testing API endpoints. FastAPI automatically generates and hosts Swagger UI, so you can use it right out of the box.
**Git**: Version control is essential, and Git is a widely used system. If not already installed, you can get it from git-scm.com.
**GitHub account**: A GitHub account is required to access the code repositories. Sign up at github.com if you haven’t already.

## Installation

1. Python
```sudo apt-get install python3```
You can then check that Python is correctly installed by running the following command in the terminal:
```python3 --version```
Once Python is installed, we want to make sure that the Python’s package manager is correctly installed.
It comes with Python’s installation, and it’s called **pip**
```pip3 --version```
2. FastAPI
We’ll set up our virtual environment by running the following command:
```python -m venv .venv```
This will create a .venv folder that will contain all packages required for the project within our project's root folder.
Now, you need to activate the environment. If you are on Mac or Linux, run the following command:
```$ source .venv/bin/activate```
This command installs FastAPI along with its recommended dependencies, including Uvicorn.
```pip install fastapi[all]```
To verify the installations, you can simply run:

```bash
fastapi --version
uvicorn --version
```

## Creating a new FastAPI project

We begin by making a project folder named fastapi_start that we’ll use as the root project folder.
Once FastAPI is installed in your environment, open your project folder with your favorite IDE and create a file called main.py.
This file is where your FastAPI application begins. Start by writing the import of the FastAPI module. Then, create an instance of the FastAPI class:

```python

from fastapi import FastAPI
app = FastAPI()

```

This instance houses the code of your application.
</hr>
Next, define your first route. Routes in FastAPI are like signposts that direct requests to the appropriate function. Start with a simple route that returns a greeting to the world:

```python

@app.get("/")
async def read_root():
    return {"Hello": "World"}
```

You’ve just created the code for your first FastAPI application.

## Understanding FastAPI basics

**Asynchronous programming** is a style of concurrent programming in which tasks are executed without blocking the execution of other tasks, improving the overall performance of your application. To integrate asynchronous programming smoothly, FastAPI leverages the async/await syntax [async](https://fastapi.tiangolo.com/async/) and automatically integrates asynchronous functions.

**Endpoints** are the points at which API interactions happen. In FastAPI, an endpoint is created by decorating a function with an HTTP method, such as ```@app.get("/")```.
This signifies a GET request to the root of your application.
**Routers** assist us in grouping our endpoints into different modules, which makes our code base easier to maintain and understand. For example, we could use one router for operations related to users and another for operations related to products.
To define a router, first create a new file in the fastapi_start folder called router_example.py. Then, create the router as follows:

```python
from fastapi import APIRouter
router = APIRouter()

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

You can now reuse it and attach the router to the FastAPI server instance in main.py:

```python

import router_example
from fastapi import FastAPI

app = FastAPI()
app.include_router(router_example.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
```

You now have the code to run the server that includes the router for the GET /items endpoint importer from another module.

## Running your first FastAPI server

To run your FastAPI application, you need to point Uvicorn to your app instance. If your file is named main.py and your FastAPI instance is called app, you can start your server like this at the
fastapi_start folder level:
```$ uvicorn main:app --reload```
The --reload flag makes the server restart after code changes, making it ideal for development.</hr>
Once the server is running, you can access your API at [server](http://127.0.0.1:8000). If you visit this URL in your browser, you’ll see the JSON response from the "/" endpoint we have just created.

### Exploring the automatic documentation

One of the most exciting features of FastAPI is its automatic documentation. When you run your FastAPI application, two documentation interfaces are automatically generated: Swagger UI and Redoc.
You can access these at [swagger](http://127.0.0.1:8000/docs) for Swagger UI and
[redoc](http://127.0.0.1:8000/redoc) for Redoc.
These interfaces provide an interactive way to explore your API and test its functionality.

## Working with Data

Setting up SQL databases
• Understanding CRUD operations with SQLAlchemy
• Integrating MongoDB for NoSQL data storage
• Working with data validation and serialization
• Working with file uploads and downloads
• Handling asynchronous data operations
• Securing sensitive data and best practices
Each topic is designed to equip you with the necessary skills and knowledge to handle data in FastAPI efficiently, ensuring your applications are not only functional but also secure and scalable.
