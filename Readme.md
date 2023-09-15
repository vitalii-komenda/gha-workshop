# GH Actions workshop

## Creating and using a venv

```bash
python3 -m venv .venv

source .venv/bin/activate
```

## Starting the database locally

```bash
docker-compose up -d tasks_db
```

## Creating a test database

```bash
docker exec -ti tasks_db /usr/local/bin/psql -U postgres

CREATE USER tests WITH PASSWORD 'tests';
CREATE DATABASE tasks_test WITH OWNER tests;
```

## Running the tests

```bash
python -m unittest discover -s tests -p 'test_*.py'
```
