# Useful Commands <!-- omit from toc -->

- [Poetry](#poetry)
  - [Export python dependencies from poetry to requirements.txt](#export-python-dependencies-from-poetry-to-requirementstxt)
  - [Show outated packages](#show-outated-packages)
- [Jupyter Lab](#jupyter-lab)
  - [Opening jupyter lab](#opening-jupyter-lab)
- [Docker](#docker)
  - [List all docker processes](#list-all-docker-processes)
  - [Building the images](#building-the-images)
  - [Starting the containers](#starting-the-containers)
  - [Stopping the containers](#stopping-the-containers)
  - [Restarting the containers](#restarting-the-containers)

## Poetry

### Export python dependencies from poetry to requirements.txt

```sh
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

### Show outated packages

```sh
poetry show --outdated
```

## Jupyter Lab

### Opening jupyter lab

```sh
jupyter lab
```

## Docker

### List all docker processes

```sh
docker ps
```

### Building the images

```sh
docker build --file Dockerfile.dev --tag backend-dev .
docker build --file Dockerfile.staging --tag backend-staging .
docker build --file Dockerfile.prod --tag backend-prod .
```

### Starting the containers

```sh
docker run --detach --name backend-dev-container --publish 80:80 backend-dev
docker run --detach --name backend-staging-container --publish 80:80 backend-staging
docker run --detach --name backend-prod-container --publish 80:80 backend-prod
```

### Stopping the containers

```sh
docker stop backend-dev-container
docker stop backend-staging-container
docker stop backend-prod-container
```

### Restarting the containers

```sh
docker restart backend-dev-container
docker restart backend-staging-container
docker restart backend-prod-container
```