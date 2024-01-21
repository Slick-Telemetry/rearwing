[![CodeQL](https://github.com/Slick-Telemetry/backend/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/Slick-Telemetry/backend/actions/workflows/codeql.yml)

# backend <!-- omit from toc -->

Slick Telemetry backend written in python with fastf1.

Table of Contents:

- [Setting up the project](#setting-up-the-project)
  - [What you'll need](#what-youll-need)
- [Development](#development)
  - [Python virtual environment](#python-virtual-environment)
    - [Installing dependencies](#installing-dependencies)
    - [Running the project](#running-the-project)
  - [Docker](#docker)
  - [Interactive API docs](#interactive-api-docs)
  - [Interactive Jupyter notebook](#interactive-jupyter-notebook)
    - [Using Jupyter Lab](#using-jupyter-lab)
    - [Running the notebook in VS Code](#running-the-notebook-in-vs-code)
  - [Running tests](#running-tests)
  - [Contribution Guidelines](#contribution-guidelines)
- [Deployment](#deployment)

## Setting up the project

### What you'll need

- [VSCode](https://code.visualstudio.com/) / [Pycharm](https://www.jetbrains.com/pycharm/)
- [Python 3.12](https://www.python.org/) (Please check [`pyproject.toml`](./pyproject.toml) for the latest supported python version)
- [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) for dependency management
- [Docker Desktop](https://docs.docker.com/desktop/) [OPTIONAL]

## Development

### Python virtual environment

#### Installing dependencies

```sh
poetry install --no-root
```

**Note**: Ensure that the python interpreter in your IDE is set to the newly created virtual environment by poetry. If you have not modified poetry configuration, you can find the virtual environment location as stated [here](https://python-poetry.org/docs/configuration/#cache-directory).

#### Running the project

- Open up a terminal in your IDE.
  - Your IDE should activate the virtual environment for you automatically.
  - If it doesn't, you can follow either of these steps:
    -  Set poetry [python interpreter path in VS Code](https://code.visualstudio.com/docs/python/environments#_working-with-python-interpreters) <u> ***OR*** </u>
    -  Run `poetry shell` <u> ***OR*** </u>
    -  Execute the `/Scripts/Activate` script from the virtual environment located [here](https://python-poetry.org/docs/configuration/#cache-directory)

- Run `python run.py` to start the server.
- Open your browser at `http://127.0.0.1/8081`.

### Docker

- Build image
  ```sh
  docker build --file Dockerfile.dev --tag backend-dev .
  ```
  **Note**: The first build will take about 10 minutes. Please be patient. Subsequent builds should be quicker (given that the image has not been prunes).
- Run container
  ```sh
  docker run --detach --name backend-dev-container --publish 8081:8081 backend-dev
  ```
- Open your browser at http://127.0.0.1/8081.
- For other docker commands, see [useful_commands.md](./useful_commands.md)

### Interactive API docs

- Once the server is running, open your browser at `http://127.0.0.1:8081/docs`.
- Alternate docs can be found at `http://127.0.0.1:8081/redoc`, provided by [redoc](https://github.com/Redocly/redoc).

### Interactive Jupyter notebook

#### Using Jupyter Lab

- The project has Jupyter Lab as a dev dependency for you to rummage through FastF1.
- Run `jupyter lab` in a new terminal and open your default browser should open automatically (if it doesn't, open browser at `http://localhost:8888/lab`).

#### Running the notebook in VS Code

- Alternatively, you can install the [Jupyer extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) and run the notebook in VS Code.
- Ensure to use the poetry python environment as the kernel.

### Running tests

```sh
poetry run pytest -rpP
```

### Contribution Guidelines

- <u> _**NEVER MERGE YOUR OWN CODE; ALWAYS RAISE A PR AGAINST `dev`!**_ </u>

- **Always pull latest changes**

  - There are several developers working on this project. Always pull/pull-rebase the latest, as necessary, from the branch you intend to commit your changes to.
  - If there are local staged/unstaged changes, please stash or discard them as appropriate and then use `git pull --rebase`.
  - If you don't want to use git CLI, to simplify these operations and have a visual representation of the git tree, we suggest to use a git GUI -
    - [Github Desktop](https://desktop.github.com/) (free)
    - [GitKraken](https://www.gitkraken.com/) (paid)
    - [Fork](https://git-fork.com/) (paid)
    - [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) (freemium)
    - [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) (free)

- **Branches**:

  - `main` is the production mainline.
  - `staging` is the staging line.
  - `dev` is the development line (_**default branch**_).

- **PR merge strategy on Github**

  - Code should flow in the following direction through branches:
    ```
    feature/bug fix -> dev -> staging -> main
    ```
  - We'll be keeping a linear commit history and so using a combination of `Rebase and merge` and `Squash and merge` merge strategies.
  - Use `Rebase and merge` as _**default**_ to ensure all commits from the branch to be merged are brought in individually to the target branch.
  - `Squash and merge` may be used _**ONLY**_ when bringing in changes from a feature/bug fix branch into `dev`.
  - To maintain linear commit history, ensure to use `push force` when:
    - Bringing `dev` on the same commit as `staging` (ie rebasing `dev` onto `staging`).
    - Bringing `staging` on the same commit as `main` (ie rebasing `staging` onto `main`).
  - [More information on git rebase](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase).
  - [More information on PR merge strategies](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github).

## Deployment

// TODO
