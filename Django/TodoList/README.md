# Todo App

![Todo Logo](https://media.istockphoto.com/id/116772376/photo/notepad-to-do-list-get-things-done.jpg?b=1&s=170667a&w=0&k=20&c=olKqBwtbJQA4tH_tC520qngYwyjcrpuHZ2eYq3EXgjk=)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

This is a simple Todo App in Django. It allows users to create, view and delete tasks.

## Features

- CRUD operations[Create, View, Update, Delete]

## Technologies Used

- Python 3.12.3
- Django 5.1.1 (or the specific version you are using)
- [HTML5 & CSS3]
- [Database - SQLite3]

## Installation

To get a copy of this project up and running on your local machine for development and testing purposes, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/john-otienoh/backender.git
   cd backender/Django/TodoList/
   ```

2. **Create a Virtual Environment:**

    ```bash
    python3 -m venv venv
    ```

3. **Activate the virtual environment:**
    On Windows

    ```bash
    venv\Scripts\activate
    ```

    On MacOS/Linux

     ```bash
    source venv/bin/activate
    ```

4. **Install Required Packages:**

     ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Set Up the database:**

     ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

3. **Access the application:**
Open your web browser and go to [Here](http://127.0.0.1:8000/todo/)  to view the application.
