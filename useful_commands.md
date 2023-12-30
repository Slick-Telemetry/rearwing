# Useful Commands <!-- omit from toc -->

- [Poetry](#poetry)
  - [Export python dependencies from poetry to requirements.txt](#export-python-dependencies-from-poetry-to-requirementstxt)
  - [Show outated packages](#show-outated-packages)
- [Jupyter Lab](#jupyter-lab)
  - [Opening jupyter lab](#opening-jupyter-lab)
- [Docker](#docker)
  - [Building the images](#building-the-images)
  - [Starting the containers](#starting-the-containers)

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

### Building the images

```sh
docker build --file Dockerfile.dev --tag backend-dev .
docker build --file Dockerfile.staging --tag backend-staging .
docker build --file Dockerfile --tag backend-prod .
```

### Starting the containers

```sh
docker run --detach --name backend-dev-container --publish 80:80 backend-dev
docker run --detach --name backend-staging-container --publish 80:80 backend-staging
docker run --detach --name backend-prod-container --publish 80:80 backend-prod
```
