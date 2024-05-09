[![CodeQL](https://github.com/Slick-Telemetry/rearwing/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/Slick-Telemetry/rearwing/actions/workflows/codeql.yml)

# rearwing <!-- omit from toc -->

Slick Telemetry backend written in python with fastf1.

Table of Contents:

- [Setting up the project](#setting-up-the-project)
  - [What you'll need](#what-youll-need)
- [Development](#development)
  - [Environment variables](#environment-variables)
  - [Python virtual environment](#python-virtual-environment)
    - [Installing dependencies](#installing-dependencies)
    - [Virtual environment sanity check](#virtual-environment-sanity-check)
    - [Poe the Poet](#poe-the-poet)
    - [Installing git hooks](#installing-git-hooks)
  - [New Relic integration](#new-relic-integration)
  - [Running the project](#running-the-project)
  - [Running tests](#running-tests)
  - [Docker](#docker)
    - [App only](#app-only)
    - [With Supabase](#with-supabase)
  - [Interactive API docs](#interactive-api-docs)
  - [Contribution Guidelines](#contribution-guidelines)
- [Deployment](#deployment)

## Setting up the project

### What you'll need

- [VSCode](https://code.visualstudio.com/) / [Pycharm](https://www.jetbrains.com/pycharm/)
- [Python 3.12](https://www.python.org/) (Please check [`pyproject.toml`](./pyproject.toml) for the latest supported python version)
- [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) for dependency management
- [Docker Desktop](https://docs.docker.com/desktop/) [OPTIONAL]

## Development

### Environment variables

- In project root, create a copy of `.env.example` as `.env`.

### Python virtual environment

#### Installing dependencies

```sh
poetry config virtualenvs.in-project true # OPTIONAL
poetry install --sync --no-root --with dev,lint,test
```

**Note**: Ensure that the python interpreter in your IDE is set to the newly created virtual environment by poetry. If you have not modified poetry configuration, you can find the virtual environment location as stated [here](https://python-poetry.org/docs/configuration/#cache-directory).

#### Virtual environment sanity check

- Your IDE should activate the virtual environment for you automatically.
- If it doesn't, you can follow either of these steps:
  - Check the path of poetry env - `poetry env info`.
  -  Set poetry [python interpreter path in VS Code](https://code.visualstudio.com/docs/python/environments#_working-with-python-interpreters) <u> ***OR*** </u>
  -  Run `poetry shell` <u> ***OR*** </u>
  -  Execute the `/Scripts/Activate` script from the virtual environment located [here](https://python-poetry.org/docs/configuration/#cache-directory).


#### Poe the Poet

https://github.com/nat-n/poethepoet

1. Check available tasks:
   ```sh
   poetry run poe
   ```
2. Execute a task:
   ```sh
   poetry run poe <task-name>
   ```
    For example, running the project formatters:
    ```sh
    poetry run poe formatters
    ```

#### Installing git hooks

```sh
poetry run poe git-hooks-setup
```

### New Relic integration

 - Create a `newrelic.ini` file at the root of the project.
 - Copy contents supplied by Pratik Borole into it.

### Running the project

- Open up a terminal in your IDE.
- Run `python run.py` to start the server.
- Open your browser at [`http://localhost:8081`](http://localhost:8081).

### Running tests

```sh
poetry run poe tests
```

### Docker

In `/docker`, create a copy of `.env.example` as `.env`.

#### App only

- Build image
  ```sh
  docker build --file Dockerfile.dev --tag rearwing-dev .
  ```
- Run container
  ```sh
  docker run --name rearwing-dev --publish 8081:8081 rearwing-dev --detach
  ```
- Open your browser at [`http://localhost:8081`](http://localhost:8081).

#### With Supabase

- Bring up the services
  ```sh
  cd docker
  docker compose --file compose.dev.yaml up --detach
  ```
- Open your browser at
  - [`http://localhost:8081`](http://localhost:8081) for app
  - [`http://localhost:8000`](http://localhost:8000) for supabase dashboard
  - Username: `supabase`
  - Password: `this_password_is_insecure_and_should_be_updated`

For other docker commands, see [useful_commands.md](./useful_commands.md).

### Interactive API docs

- Once the server is running, open your browser at [`http://localhost/docs`](http://localhost/docs).
- Alternate docs can be found at [`http://localhost/redoc`](http://localhost/redoc), provided by [redoc](https://github.com/Redocly/redoc).

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
  - `dev` is the development line (***default branch***).
- **PR merge strategy on Github**
  - Code should flow in the following direction through branches:
    ```
    feature/bug fix -> dev -> main
    ```
  - We'll be keeping a linear commit history and so using a combination of `Rebase and merge` and `Squash and merge` merge strategies.
  - Use `Rebase and merge` as ***default*** to ensure all commits from the branch to be merged are brought in individually to the target branch.
  - `Squash and merge` may be used ***ONLY*** when bringing in changes from a feature/bug fix branch into `dev`.
  - To maintain linear commit history, ensure to use `push force` when:
    - Bringing `dev` on the same commit as `main` (ie rebasing `dev` onto `main`).
  - [More information on git rebase](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase).
  - [More information on PR merge strategies](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github).
- **Jira issue linking**
  - Commits and PRs ***must*** be linked to a Jira issue.
  - To do so, include the Jira issue key in the PR title and/or the commit message after the conventional commit type.
  - [More information on Jira smart commits](https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/).

## Deployment

We currently have a test deployment in linode. The deployment is done manually.

We're using pm2, a process manager for Node.js applications, to run the application. The configuration for pm2 can be found in the `process.config.js` file.

For pm2 commands, see [useful_commands.md](./useful_commands.md).
