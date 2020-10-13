# pull official base image
FROM python:3.8.1-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY ./requirements.txt /usr/src/app/requirements.txt

# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/src/app/requirements.txt \
    && rm -rf /root/.cache/pip

# copy project
COPY . /usr/src/app/

# download medicare data
#ADD https://data.cms.gov/api/views/fs4p-t5eq/rows.csv?accessType=DOWNLOAD&bom=true&format=true /usr/files/medicare_data.csv

RUN mkdir /usr/files
RUN chmod 775 /usr/files
RUN pip install gdown
RUN gdown --id 1PZway6yRSYLVbwXB9wYKWPFp395037at --output /usr/files/science.db.zip
RUN chmod 775 /usr/files/science.db.zip
RUN unzip /usr/files/science.db.zip -d /usr/files
