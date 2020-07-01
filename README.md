# notelog

A topic-based note-taking web application

## Summary

- [Getting Started](#getting-started)
- [Running the tests](#running-the-tests)
- [Development Process](#development-process)
- [Built With](#built-with)
- [Authors](#authors)

## Getting Started

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on how to deploy the project on a live system.

### Prerequisites

Project based on Docker containers. As basic prerequisites, you need to get:

- **Docker v.19.03.11-ce** (Linux) or **Docker Machine** (Windows, MacOS)
- **Docker Compose v.1.26.0**

### Installing

Install Docker and Docker Compose on your machine using official guides:

- **Docker**: [link](https://docs.docker.com/get-docker/)
- **Docker Compose**: [link](https://docs.docker.com/compose/install/)

Clone repository to your machine

    $ git clone https://github.com/Hephest/notelog.git

Create `.env` file inside project root directory with needed data

    DJANGO_SECRET_KEY = <YOUR_SECRET_KEY>

    DB_NAME = <YOUR_DB_NAME>
    DB_USER = <YOUR_DB_USER>
    DB_PASSWORD = <YOUR_DB_PASSWORD>
    DB_HOST = 'db'
    DB_PORT = 5432

> Standard `DB_HOST` is `db` and `DB_PORT` is `5432`. To change that, update your `docker-compose.yml`

Run `docker-compose`

    $ docker-compose up

After successful build, you receive in terminal something like this:

    Starting notelog_db_1 ... done
    Starting notelog_web_1 ... done
    Attaching to notelog_db_1, notelog_web_1
    db_1   | 
    db_1   | PostgreSQL Database directory appears to contain a database; Skipping initialization
    db_1   | 
    db_1   | 2020-06-29 07:49:27.632 UTC [1] LOG:  starting PostgreSQL 12.3 (Debian 12.3-1.pgdg100+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 8.3.0-6) 8.3.0, 64-bit
    ...
    web_1  | Django version 3.0.7, using settings 'app.settings'
    web_1  | Starting development server at http://0.0.0.0:8000/
    web_1  | Quit the server with CONTROL-C.

## Running the tests

To run tests inside a Docker container

    $ docker-compose run --no-deps --rm web python manage.py test -v 2

> Note: `-v 2` parameter is optional, just for logging improvement

## Development Process

### Environment

> Note: do not use example data in production, make sure to change all data accordingly to your project!

All security sensitive data will contains in `.env` file, located at project root.

#### Example

`.env` structure

    # Django configuration
    DJANGO_SECRET_KEY = 'lu5ien0giye&j1s#iby_89a1zx((9!32+-6@%d_54ll4b%tn+b'

    # PostgreSQL database configuration
    DB_NAME = 'postgres'
    DB_USER = 'postgres'
    DB_PASSWORD = 'postgres'
    DB_HOST = 'db'
    DB_PORT = 5432

### Django

To run Django administrative commands, use `docker-compose`

    sudo docker-compose run web <COMMAND>

#### Examples

Create a new superuser (admin)

    sudo docker-compose run web python manage.py createsuperuser

Create a new app inside Django project

    sudo docker-compose run web django-admin startapp <APP_NAME>

Perform database migrations

    sudo docker-compose run web manage.py makemigrations
    sudo docker-compose run web manage.py migrate

## Built With

- [Django](https://www.djangoproject.com/) - A high-level Python Web framework.
- [PostgreSQL](https://www.postgresql.org/) -  A powerful, open source object-relational database system.
- [Django REST Framework](https://www.django-rest-framework.org/) - a powerful and flexible toolkit for building Web APIs.

## Authors

- **Vladyslav Asaievych** - *Main development workflow* - [Hephest](https://github.com/Hephest)