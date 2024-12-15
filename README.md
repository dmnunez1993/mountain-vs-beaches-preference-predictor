# Mountain vs Beaches Predictor Application

An application that implements a Mountain vs Beaches predictor project as a web application.

### Dependencies

- [docker](https://www.docker.com/) - Used for the dev environment and for deployment

### Set up the dev environment

Make sure Docker is installed. The dev environment should work with Linux, macOS and Windows (through WSL2)

To build the dev environment:

    ./dev_env build

To run the dev environment:

    ./dev_env

### Backend Development (w/ FastAPI)

In order to start developing the backend, you need to run the following in the root of the repository:

    cd backend
    cp .env.example .env
    pip install -r requirements.txt

Then, to run the app:

    python ./api.py

To run the migrations for the project:

    alembic upgrade head

To create a new migration:

    alembic revision --autogenerate -m "<migration_name>"

To downgrade a migration previously created:

    alembic downgrade -1
