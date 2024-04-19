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
- [PM2](#pm2)
  - [Start process](#start-process)
  - [Stop process](#stop-process)
  - [Check process status](#check-process-status)

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
docker build --file Dockerfile.dev --tag rearwing-dev .
docker build --file Dockerfile.prod --tag rearwing-prod .
```

#### Start the containers

```sh
docker run --name rearwing-dev --publish 8081:8081 rearwing-dev --detach
docker run --name rearwing-prod --publish 80:80 rearwing-prod --detach
```

#### Stop the containers

```sh
docker stop rearwing-dev
docker stop rearwing-prod
```

#### Restart the containers

```sh
docker restart rearwing-dev
docker restart rearwing-prod
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

## PM2

### Start process

```sh
pm2 start process.config.js
```

### Stop process

```sh
pm2 stop process.config.js
```

### Check process status

```sh
pm2 status
```
