[![CodeQL](https://github.com/Slick-Telemetry/backend/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/Slick-Telemetry/backend/actions/workflows/codeql.yml)

# backend <!-- omit from toc -->

Slick Telemetry backend written in python.

Table of Contents:

- [Setting up the project](#setting-up-the-project)
  - [What you'll need](#what-youll-need)
  - [Installing dependencies](#installing-dependencies)
- [Development](#development)
  - [Running the project](#running-the-project)
  - [Interactive API docs](#interactive-api-docs)
  - [Interactive Jupyter notebook](#interactive-jupyter-notebook)
    - [Using Jupyter Lab](#using-jupyter-lab)
    - [Running the notebook in VS Code](#running-the-notebook-in-vs-code)
  - [Contribution Guidelines](#contribution-guidelines)
- [Deployment](#deployment)

## Setting up the project

### What you'll need

- [VSCode](https://code.visualstudio.com/) / [Intellij Pycharm](https://www.jetbrains.com/pycharm/)
- [Python 3.11](https://www.python.org/) (Please check `pyproject.toml` for the latest supported python version)
- [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) for dependency management

### Installing dependencies

```sh
poetry install --no-root
```

**Note**: Ensure that the python intepreter in your IDE is set to the newly created virtual environment by poetry. If you have not modified poetry configuration, you can find the virtual environment location as stated [here](https://python-poetry.org/docs/configuration/#cache-directory).

## Development

### Running the project

- Open up a terminal in your IDE.
  - Your IDE should activate the virtual environment for you automatically.
  - If it doesnt, you can execute the `/Scripts/Activate` script from the virtual environment.
- Run `uvicorn main:app --reload` to start the server.
- Open your browser at `http://127.0.0.1/8000`.

### Interactive API docs

- Once the server is running, open your browser at `http://127.0.0.1:8000/docs`.
- Alternate docs can be found at `http://127.0.0.1:8000/redoc`, provided by [redoc](https://github.com/Redocly/redoc).

### Interactive Jupyter notebook

#### Using Jupyter Lab

- The project has Jupyter Lab as a dev dependency for you to rummage through FastF1.
- Run `jupyter lab` in a new terminal and open your default browser should open automatically (if it doesn't, open browser at `http://localhost:8888/lab`).

#### Running the notebook in VS Code

- Alternatively, you can install `https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter` and run the notebook in VS Code.
- Ensure to use the poetry python environment as the kernel.

### Contribution Guidelines

- <u> _**NEVER MERGE YOUR OWN CODE; ALWAYS RAISE A PR AGAINST `dev`!**_ </u>

- **Always pull latest changes**

  - There are several developers working on this project. Always pull the latest from the line you intend to commit your changes to. Since we are using `Rebase and merge` PR merge strategy (more information below), there would be times when `git pull` will fail.
  - If there are no local staged/unstaged changes, you can use `git pull --force`.
  - If there are local staged/unstaged changes, please stash or discard them as appropriate and then use `git pull --force`.
  - If you don't want to use git CLI, to simplify these operations and have a visual representation of the git tree, we suggest to use a git GUI -
    - [Github Desktop](https://desktop.github.com/) (free)
    - [GitKraken](https://www.gitkraken.com/) (paid)
    - [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) (freemium)
    - [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) (free)

- **Branches**:

  - `main` is the production mainline.
  - `dev` is the development line.

- **PR merge strategy on Github**

  - We'll be keeping a clean commit history and so only using `Rebase and merge` and `Squash and merge` merge strategies.
  - Opt for `Rebase and merge` as the _**default**_ one to ensure all commits from the branch to be merged are brought in individually to the target branch.
  - `Squash and merge` can be used when the commits _**DON'T**_ need to be individually brought in to the target branch.
  - [More information](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github).

## Deployment

// TODO
