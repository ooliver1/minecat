FROM --platform=amd64 python:3.10-slim-buster

WORKDIR /bot

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY manager/pyproject.toml manager/poetry.lock ./

RUN poetry install --no-root --only main

COPY . .

ENTRYPOINT ["poetry", "run", "python3"]
CMD ["-m", "manager"]
