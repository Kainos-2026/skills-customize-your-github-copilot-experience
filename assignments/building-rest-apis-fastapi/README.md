# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build RESTful APIs using the FastAPI framework in Python, including creating endpoints, handling HTTP requests and responses, and using Pydantic for data validation.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI application and create a simple GET endpoint that returns a welcome message.

#### Requirements
Completed program should:
- Install FastAPI and Uvicorn
- Create a FastAPI app instance
- Define a GET endpoint at "/" that returns a JSON response with a welcome message
- Run the server and verify the endpoint works

### 🛠️ Add POST Endpoint with Data Validation

#### Description
Add a POST endpoint that accepts user data, validates it using Pydantic models, and returns a processed response.

#### Requirements
Completed program should:
- Define a Pydantic model for user data (e.g., name and age)
- Create a POST endpoint at "/users" that accepts the user data
- Validate the input data automatically
- Return a response confirming the user creation with the provided data