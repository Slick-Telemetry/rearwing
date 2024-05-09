## 0.7.0 (2024-05-09)

### Feat

- add /fastest-sectors path

## 0.6.1 (2024-04-19)

### Fix

- **cors**: add 127.0.0.1 to CORS origins
- **laps**: ignore error message

### Refactor

- rename backend to rearwing
- move fastapi app init to main.py
- move app config to __init__.py

## 0.6.0 (2024-04-07)

### Feat

- BACK-8 new relic integration
- BACK-53 added /split-qualifying-laps path

### Fix

- save resources when getting default year
- **cache**: BACK-54 disable cache
- fixed typos in project config

### Refactor

- **test**: use client_with_auth
- use version from app/__init__.py
- extract FRONTEND_URL to .env

## 0.5.1 (2024-03-17)

### Fix

- **ci**: updated conditions for steps

## 0.5.0 (2024-03-16)

### Feat

- **security**: BACK-48 security token for accessing endpoints

### Fix

- **tests**: fixed failing tests

## 0.4.0 (2024-03-07)

### Feat

- BACK-40 added /telemetry path

### Fix

- **next-event**: use pydantic.model_validate_json

### Refactor

- updated constants

## 0.3.0 (2024-02-27)

### Feat

- BACK-39 added /laps path
- BACK-31 upgraded to python 3.12.2
- BACK-38 added linter and typecheck
- BACK-36 added poethepoet poetry plugin

### Fix

- **logging**: less noise during development

### Refactor

- **tests**: BACK-44 moved tests to a separate folder

## 0.2.0 (2024-02-12)

### Feat

- added timing middleware
- BACK-32 added /next-event path
- BACK-26 supabase self-host initial setup
- **results**: BACK-14 session is optional with default as race
- BACK-13 /schedule now provides the year

### Fix

- **schedule**: BACK-24 exclude testing events
- BACK-22 added missing favicon.ico
- **results**: BACK-19 don't fetch laps

### Refactor

- better organized docker installation

## 0.1.0 (2024-01-28)

### Feat

- cors support for local dev
