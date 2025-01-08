FROM python:3.10-alpine

RUN apk add postgresql-libs gcc g++ musl-dev postgresql-dev

RUN mkdir /inference
RUN mkdir /train
RUN mkdir /data

# Setup code
COPY ./inference/requirements.txt /inference/requirements.txt
WORKDIR /inference

RUN pip install -r requirements.txt

COPY ./inference/. /inference/

COPY ./train/. /train
COPY ./data /data

RUN cd /train/ && ./train_model.py -i /data/raw/mountains_vs_beaches_preferences.csv -o /inference/prediction_model/lr.pkl

# Set up pythonpath
ENV PYTHONPATH=/inference

CMD ["python3", "cmd/api.py"]
