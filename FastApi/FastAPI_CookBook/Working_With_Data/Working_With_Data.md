# Working with Data

You will embark on a journey of working with data in FastAPI, where you’ll learn
the intricacies of integrating, managing, and optimizing data storage using both Structured Query Language (SQL) and NoSQL databases. We’ll cover how FastAPI, combined with powerful database tools, can create efficient and scalable data management solutions.</hr>
Setting up SQL databases

1. Understanding CRUD operations with SQLAlchemy
2. Integrating MongoDB for NoSQL data storage
3. Working with data validation and serialization
4. Working with file uploads and downloads
5. Handling asynchronous data operations
6. Securing sensitive data and best practices
Each topic is designed to equip you with the necessary skills and knowledge to handle data in FastAPI efficiently, ensuring your applications are not only functional but also secure and scalable.

## Setting up SQL databases

FastAPI’s compatibility with SQL databases is facilitated through ORMs. The most popular one is SQLAlchemy.
```pip install sqlalchemy```

Once installed, the next step is to configure SQLAlchemy so that it can work with FastAPI. This involves setting up the database connection
SQLAlchemy acts as the bridge between your Python code and the database, allowing you to interact with the database using Python classes and objects rather than writing raw SQL queries.
