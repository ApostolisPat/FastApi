# FastAPI Projects

This repository contains three FastAPI-based projects, each demonstrating different use cases and functionalities of the FastAPI framework. Below is an overview of each project.

---

## 1. SimpleToDoAPI

A simple To-Do application that allows users to manage their tasks.

### Features:
- Add new tasks with a description and completion status.
- Retrieve all tasks with optional limits.
- Retrieve a specific task by its ID.

### Endpoints:
- `GET /` - Root endpoint.
- `POST /items` - Add a new task.
- `GET /items` - List tasks with an optional limit.
- `GET /items/{item_id}` - Retrieve a specific task by ID.

### How to Run:
1. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```
2. Start the server:
   ```bash
   uvicorn main:app --reload
   ```
3. Access the API documentation at:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 2. InventoryManagementSystemAPI

An inventory management system for managing items with attributes like name, price, and brand.

### Features:
- Add new items to the inventory.
- Retrieve items by ID or name.
- Update existing items.
- Delete items from the inventory.

### Endpoints:
- `GET /get-item/{item_id}` - Retrieve an item by ID.
- `GET /get-by-name` - Retrieve an item by name.
- `POST /create-item/{item_id}` - Add a new item.
- `PUT /update-item/{item_id}` - Update an existing item.
- `DELETE /delete-item` - Delete an item by ID.

### How to Run:
1. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```
2. Start the server:
   ```bash
   uvicorn main:app --reload
   ```
3. Access the API documentation at:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 3. BlogAPI (3rd Project)

A fully-featured blog application with user authentication, blog management, and database integration.

### Features:
- User authentication with JWT tokens.
- CRUD operations for blogs.
- User management.
- SQLite database integration using SQLAlchemy.

### Endpoints:
- **Authentication**:
  - `POST /login` - User login and token generation.
- **Users**:
  - `POST /user` - Create a new user.
  - `GET /user/{id}` - Retrieve a user by ID.
- **Blogs**:
  - `GET /blog` - Retrieve all blogs.
  - `POST /blog` - Create a new blog.
  - `GET /blog/{id}` - Retrieve a specific blog by ID.
  - `PUT /blog/{id}` - Update a blog.
  - `DELETE /blog/{id}` - Delete a blog.

### How to Run:
1. Install dependencies:
   ```bash
   pip install -r app/requirements.txt
   ```
2. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```
3. Access the API documentation at:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Requirements

Each project requires Python 3.9+ and the following dependencies:
- FastAPI
- Uvicorn
- SQLAlchemy (for BlogAPI)
- Passlib (for password hashing in BlogAPI)
- Python-Jose (for JWT token generation in BlogAPI)

Install dependencies for each project using the provided `requirements.txt` file where applicable.

---

## Acknowledgment

This project was inspired by the tutorial from [Bitfumes](https://www.youtube.com/@Bitfumes).  
Special thanks to the video: [FastAPI Crash Course](https://www.youtube.com/watch?v=7t2alSnE2-I&ab_channel=Bitfumes) for providing valuable insights and guidance.

