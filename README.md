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

### Training the prediction model

To train the model, run the following commands in the root of the repository:

    cd train
    ./train_model.py -i ../data/raw/mountains_vs_beaches_preferences.csv -o ../inference/prediction_model/lr.pkl

Note that both the input path (-i) and the output path (-o) can be modified if necessary.

### Inference (w/ FastAPI)

In order to start developing the inference, you need to run the following in the root of the repository:

    cd inference
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

### Deployment

To prepare the production environment, run the following in the root of the repository:

    ./deployer build

To prepare the env file for production:

    cp prod/.env.example prod/.env

Open this file with a text editor and adjust the parameters for the target server and domain. It is important to differentiate between NGINX_BACKEND_HOST and NGINX_END_USER_APP_HOST. Both should be different subdomains. As an example:

    NGINX_BACKEND_HOST=api.mvpb.com
    NGINX_END_USER_APP_HOST=mvpb.com

The reason for this is that the REST API for inference can operate independently of the end-user application, which serves solely for demonstration purposes.

To run the production environment in unattended mode:

    ./deployer deploy

In case it is needed for debugging purposes, the production environment can be started with logging:

    ./deployer start

To stop the production environment:

    ./deployer stop

To clear the production environment entirely:

    ./deployer clear
