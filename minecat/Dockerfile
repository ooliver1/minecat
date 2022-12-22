FROM --platform=amd64 python:3.10-slim-buster

WORKDIR /bot

RUN pip install poetry

COPY minecat/pyproject.toml minecat/poetry.lock ./

RUN poetry install --no-root --only main

COPY . .

ENTRYPOINT ["poetry", "run", "python3"]
CMD ["-m", "minecat"]
