# Flask Authentication

Here's a demo of JWT authentication implemented by Flask with usage of a relational database, offers RESTful endpoints for registration, authentication and modification of user.

## Launch

1. Prerequiste: `docker` and `docker-compose` already installed
2. Run `docker-compose build --no-cache` to build image
3. Run `docker-compose up` to run in container. Use `-d` argument to run it in background

## Development

1. Prerequiste: [`pipenv`](https://pypi.org/project/pipenv/) already installed, or convert the Pipfile into `requirements.txt` for using `virtualenv` if you wish
2. Run `pipenv install`
3. Get in the virtual environment: `pipenv shell`

## CLI

Use `flask` to view all CLI commands in virtual environment

## Routes and documentation

Here are the endpoints implemented in application:

```
Endpoint           Methods   Rule
-----------------  --------  --------------------------
api.auth_login     POST      /api/v1/auth/login
api.auth_register  POST      /api/v1/auth/register
api.auth_user      GET, PUT  /api/v1/auth/user
api.doc            GET       /api/v1/ui
api.root           GET       /api/v1/
api.specs          GET       /api/v1/swagger.json
restx_doc.static   GET       /swaggerui/<path:filename>
static             GET       /static/<path:filename> 
```

By using [`flask-restx`](https://flask-restx.readthedocs.io/en/latest/), a swagger documentation is generated when application is launched.

Run the application by `docker-compose up` or `flask run` in virtual environment, then view the documentation at `http://0.0.0.0:8000/api/v1/ui`.
