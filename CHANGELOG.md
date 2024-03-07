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
