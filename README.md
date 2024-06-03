# Python CRUD Keycloak Secured API
Basic Python 3 CRUD API solution with FastAPI and secured by keycloak.

This program was developed according with Python's good practices and based on [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/).

### Version
1.0.0


## Resources
* [Python 3](https://docs.python.org/3/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [PyJWT](https://pyjwt.readthedocs.io/en/stable/)
* [requests](https://docs.python-requests.org/en/v2.0.0/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)


## Getting Started

These instructions will guide you to copy the project from the repository and run it.

### Prerequisites

Things you need to have installed:
* [Python](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
* [FastAPI](https://fastapi.tiangolo.com/#installation)
* [PyJWT](https://pyjwt.readthedocs.io/en/stable/installation.html)
* [requests](https://docs.python-requests.org/en/v2.0.0/user/install/#install)
* [python-dotenv](https://pypi.org/project/python-dotenv/#getting-started)
* [uvicorn](https://www.uvicorn.org/)
* [pytest](https://pytest.org/en/latest/contents.html)

### Local Installation
Basically clone the project from the remote repository to the local machine, using the git commands.

```
$git clone [URL].git
```

### Create virtual environment 
To create and activate the Python virtual environment run the commands:
```
$python -m venv env
$source env/bin/activate
```

### Environment Variables
Ensure that the .env file exists and has the environment variables for your application:
* KEYCLOAK_VALIDATE_TOKEN_URL - The keycloak URL to validate the token 
* KEYCLOAK_CLIENT_ID - The keycloak client ID, of the current service, to validate the token
* KEYCLOAK_CLIENT_SECRET - The keycloak client secret, of the current service, to validate the token

### Run
To run the project, first check that the FastAPI, PyJWT, requests, python-dotenv libraries are installed, then run the python command.
```
$python main.py
```

### Documentation

Run the application and then access to the API documentation
* [API Documentation](http://localhost:8081/docs)


##### Public Endpoints
* [GET API Health Check](http://localhost:8081/api/tasks/health)
* [GET task by ID](http://localhost:8081/api/tasks/{id})
* [GET All tasks](http://localhost:8081/api/tasks)

##### Private Endpoints
* [POST Create Task](http://localhost:8081/api/tasks)
* [PUT Update Task](http://localhost:8081/api/tasks/{id})
* [DELETE Delete Task](http://localhost:8081/api/tasks/{id})

### Test
To run the unit tests, first check that the FastAPI, PyJWT, requests, python-dotenv and pytest libraries are installed, then run the python command:
```
$pytest tests/
```

## Authors

* **BEOM &copy; 2024**