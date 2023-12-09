# Useful Commands <!-- omit from toc -->

- [1. Poetry](#1-poetry)
  - [1.1. Export python dependencies from poetry to requirements.txt](#11-export-python-dependencies-from-poetry-to-requirementstxt)

## 1. Poetry

### 1.1. Export python dependencies from poetry to requirements.txt

```sh
poetry export --without-hashes --format=requirements.txt > requirements.txt
```
