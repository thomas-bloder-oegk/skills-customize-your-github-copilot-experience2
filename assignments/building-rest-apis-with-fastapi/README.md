# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with the FastAPI framework. You will practice creating routes, returning JSON data, validating request bodies, and using HTTP status codes for common API actions.

## 📝 Tasks

### 🛠️	Create a FastAPI Application

#### Description
Set up a FastAPI app that can run locally and respond to basic requests.

#### Requirements
Completed program should:

- Create a FastAPI application object named `app`.
- Include a `GET /` route that returns a welcome message as JSON.
- Include a `GET /health` route that returns an API status message.
- Run successfully with Uvicorn.


### 🛠️	Build Item API Routes

#### Description
Create REST API routes that let users view, create, and retrieve items from an in-memory list.

#### Requirements
Completed program should:

- Store items in a Python list or dictionary while the app is running.
- Include a `GET /items` route that returns all items.
- Include a `GET /items/{item_id}` route that returns one matching item.
- Include a `POST /items` route that creates a new item from JSON input.
- Return a helpful error message when an item ID does not exist.


### 🛠️	Add Validation and Status Codes

#### Description
Use Pydantic models and FastAPI response tools to make the API behave more like a real web service.

#### Requirements
Completed program should:

- Use a Pydantic model to validate each new item's name, description, and price.
- Return `201 Created` when a new item is added successfully.
- Return `404 Not Found` when a requested item does not exist.
- Prevent invalid item data from being accepted by the API.
- Keep route names and response messages clear and consistent.