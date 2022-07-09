FROM --platform=amd64 python:3.10-slim-buster

WORKDIR /manager

RUN apt update && apt install git -y && apt clean

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-dev

COPY . .

ENTRYPOINT ["poetry", "run", "python3"]
CMD ["manage.py"]
