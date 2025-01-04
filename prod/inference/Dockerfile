FROM python:3.10-alpine

RUN apk add postgresql-libs gcc g++ musl-dev postgresql-dev

RUN mkdir /inference

# Setup code
COPY ./inference/requirements.txt /inference/requirements.txt
WORKDIR /inference

RUN pip install -r requirements.txt

COPY ./inference/. /inference/

# Set up pythonpath
ENV PYTHONPATH=/inference

CMD ["python3", "cmd/api.py"]
