# notelog

A topic-based note-taking web application

## Summary

- [Getting Started](#getting-started)
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
    db_1   | 2020-06-29 07:49:27.632 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
    db_1   | 2020-06-29 07:49:27.632 UTC [1] LOG:  listening on IPv6 address "::", port 5432
    db_1   | 2020-06-29 07:49:27.644 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
    db_1   | 2020-06-29 07:49:27.690 UTC [26] LOG:  database system was shut down at 2020-06-29 07:28:18 UTC
    db_1   | 2020-06-29 07:49:27.701 UTC [1] LOG:  database system is ready to accept connections
    web_1  | Watching for file changes with StatReloader
    web_1  | Performing system checks...
    web_1  | 
    web_1  | System check identified no issues (0 silenced).
    web_1  | 
    web_1  | You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    web_1  | Run 'python manage.py migrate' to apply them.
    web_1  | June 29, 2020 - 07:49:29
    web_1  | Django version 3.0.7, using settings 'app.settings'
    web_1  | Starting development server at http://0.0.0.0:8000/
    web_1  | Quit the server with CONTROL-C.

## Development Process

To run Django administrative commands, use `docker-compose`

    sudo docker-compose run web <COMMAND>

### Examples

Create a new app inside Django project

    sudo docker-compose run web django-admin startapp <APP_NAME>

Perform database migrations

    sudo docker-compose run web manage.py makemigrations
    sudo docker-compose run web manage.py migrate

## Built With

- [Django](https://www.djangoproject.com/) - A high-level Python Web framework.
- [PostgreSQL](https://www.postgresql.org/) -  A powerful, open source object-relational database system.

## Authors

- **Vladyslav Asaievych** - *Main development workflow* - [Hephest](https://github.com/Hephest)