ARG BASE_IMAGE=python:3.10-slim-bullseye

FROM ${BASE_IMAGE}

ENV PYTHONWARNINGS=ignore \
    USER_APP=bot \
    APP_DIR=/app

WORKDIR $APP_DIR
RUN useradd -ms /bin/bash $USER_APP

RUN apt-get update && apt-get upgrade -y

COPY ./ ./

RUN pip install -r requirements.txt

RUN chown -R $USER_APP. $APP_DIR
USER $USER_APP
