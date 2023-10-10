ARG BASE_IMAGE=python:3.10-slim-bullseye

FROM ${BASE_IMAGE}

ENV PYTHONWARNINGS=ignore \
    USER_APP=bot \
    APP_DIR=/app

WORKDIR $APP_DIR

RUN apt-get update && apt-get upgrade -y

RUN useradd -ms /bin/bash $USER_APP

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./

RUN chown -R $USER_APP. $APP_DIR
USER $USER_APP
