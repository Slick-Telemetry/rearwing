# Useful Commands <!-- omit from toc -->

- [Poetry](#poetry)
  - [Export python dependencies from poetry to requirements.txt](#export-python-dependencies-from-poetry-to-requirementstxt)
  - [Show outdated packages](#show-outdated-packages)
  - [Run tests using pytest](#run-tests-using-pytest)
- [Git hooks](#git-hooks)
  - [Install git hooks](#install-git-hooks)
  - [Updating hooks automatically](#updating-hooks-automatically)
- [Docker](#docker)
  - [Dockerfile](#dockerfile)
    - [List all docker processes](#list-all-docker-processes)
    - [Build the images](#build-the-images)
    - [Start the containers](#start-the-containers)
    - [Stop the containers](#stop-the-containers)
    - [Restart the containers](#restart-the-containers)
  - [Compose](#compose)
    - [List all docker processes](#list-all-docker-processes-1)
    - [Build the services](#build-the-services)
    - [Bring up the services](#bring-up-the-services)
    - [Build and bring up the services](#build-and-bring-up-the-services)

## Poetry

### Export python dependencies from poetry to requirements.txt

```sh
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

### Show outdated packages

```sh
poetry show --outdated
```

### Run tests using pytest

```sh
 # pytest -rpP
 poetry poe tests
```

## Git hooks

### Install git hooks

```sh
# pre-commit install --hook-type commit-msg --hook-type pre-push --hook-type pre-commit
poetry poe git-hooks-setup
```

### Updating hooks automatically

```sh
# pre-commit autoupdate
poetry poe git-hooks-update
```

## Docker

### Dockerfile

#### List all docker processes

```sh
docker ps
```

#### Build the images

```sh
docker build --file Dockerfile.dev --tag backend-dev .
docker build --file Dockerfile.prod --tag backend-prod .
```

#### Start the containers

```sh
docker run --name backend-dev --publish 8081:8081 backend-dev --detach
docker run --name backend-prod --publish 80:80 backend-prod --detach
```

#### Stop the containers

```sh
docker stop backend-dev
docker stop backend-prod
```

#### Restart the containers

```sh
docker restart backend-dev
docker restart backend-prod
```

### Compose

#### List all docker processes

```sh
docker compose --file compose.dev.yaml ps
```

#### Build the services

```sh
docker compose --file compose.dev.yaml build
```

#### Bring up the services

```sh
docker compose --file compose.dev.yaml up --detach
```


#### Build and bring up the services

```sh
docker compose --file compose.dev.yaml up --build --detach
```
