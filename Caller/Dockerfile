FROM ubuntu:14.04

ENV HOME /home

# Update the repository sources list
RUN apt-get update && apt-get install -qy \
        #autofs \
        build-essential \
        curl \
        git \
        postgresql-client \
        python-dev \
        python-pip \
        libssl-dev \
        libpq-dev \
        python-Psycopg2 \
        vim

RUN psql -h ${DB_HOST} -U postgres && pip install psycopg2

ENTRYPOINT /bin/bash
