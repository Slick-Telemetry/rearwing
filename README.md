[![CodeQL](https://github.com/Slick-Telemetry/backend/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/Slick-Telemetry/backend/actions/workflows/codeql.yml)

# backend <!-- omit from toc -->

Slick Telemetry backend written in python with fastf1.

Table of Contents:

- [Setting up the project](#setting-up-the-project)
  - [What you'll need](#what-youll-need)
- [Development](#development)
  - [Python virtual environment](#python-virtual-environment)
    - [Installing dependencies](#installing-dependencies)
    - [Virtual environment sanity check](#virtual-environment-sanity-check)
    - [Installing git hooks](#installing-git-hooks)
    - [Running the project](#running-the-project)
  - [Docker](#docker)
    - [App only](#app-only)
    - [With Supabase](#with-supabase)
  - [Interactive API docs](#interactive-api-docs)
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
poetry config virtualenvs.in-project true # OPTIONAL
poetry install --sync --no-root
```

**Note**: Ensure that the python interpreter in your IDE is set to the newly created virtual environment by poetry. If you have not modified poetry configuration, you can find the virtual environment location as stated [here](https://python-poetry.org/docs/configuration/#cache-directory).

#### Virtual environment sanity check

- Your IDE should activate the virtual environment for you automatically.
- If it doesn't, you can follow either of these steps:
  - Check the path of poetry env - `poetry env info`.
  -  Set poetry [python interpreter path in VS Code](https://code.visualstudio.com/docs/python/environments#_working-with-python-interpreters) <u> ***OR*** </u>
  -  Run `poetry shell` <u> ***OR*** </u>
  -  Execute the `/Scripts/Activate` script from the virtual environment located [here](https://python-poetry.org/docs/configuration/#cache-directory).

#### Installing git hooks

Run this command in the python environment.

```sh
pre-commit install --hook-type commit-msg --hook-type pre-push --hook-type pre-commit
```

#### Running the project

- Open up a terminal in your IDE.
- Run `python run.py` to start the server.
- Open your browser at `http://127.0.0.1:8081`.

### Docker

#### App only

- Build image
  ```sh
  docker build --file Dockerfile.dev --tag backend-dev .
  ```
- Run container
  ```sh
  docker run --detach --name backend-dev --publish 8081:8081 backend-dev
  ```
- Open your browser at `http://127.0.0.1/8081`.

#### With Supabase

- Bring up the services
  ```sh
  docker compose --detach --file compose.dev.yaml up
  ```
- Open your browser at
  - `http://127.0.0.1/8081` for app
  - `http://127.0.0.1/8081` for supabase dashboard
  - Username: `supabase`
  - Password: `this_password_is_insecure_and_should_be_updated`

For other docker commands, see [useful_commands.md](./useful_commands.md)

### Interactive API docs

- Once the server is running, open your browser at `http://127.0.0.1:8081/docs`.
- Alternate docs can be found at `http://127.0.0.1:8081/redoc`, provided by [redoc](https://github.com/Redocly/redoc).

### Running tests

```sh
poetry run pytest -rpP
```

### Contribution Guidelines

- <u> ***NEVER MERGE YOUR OWN CODE; ALWAYS RAISE A PR AGAINST `dev`!*** </u>
- Follow [conventional commit format](https://www.conventionalcommits.org/en/v1.0.0/) when authoring commit messages.
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
  - `dev` is the development line (***default branch***).
- **PR merge strategy on Github**
  - Code should flow in the following direction through branches:
    ```
    feature/bug fix -> dev -> staging -> main
    ```
  - We'll be keeping a linear commit history and so using a combination of `Rebase and merge` and `Squash and merge` merge strategies.
  - Use `Rebase and merge` as ***default*** to ensure all commits from the branch to be merged are brought in individually to the target branch.
  - `Squash and merge` may be used ***ONLY*** when bringing in changes from a feature/bug fix branch into `dev`.
  - To maintain linear commit history, ensure to use `push force` when:
    - Bringing `dev` on the same commit as `staging` (ie rebasing `dev` onto `staging`).
    - Bringing `staging` on the same commit as `main` (ie rebasing `staging` onto `main`).
  - [More information on git rebase](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase).
  - [More information on PR merge strategies](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github).
- **Jira issue linking**
  - Commits and PRs ***must*** be linked to a Jira issue.
  - To do so, include the Jira issue key in the PR title and/or the commit message after the conventional commit type.
  - [More information on Jira smart commits](https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/).

## Deployment

// TODO
