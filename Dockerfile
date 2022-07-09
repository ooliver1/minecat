FROM --platform=amd64 python:3.10-slim-buster

WORKDIR /bot

RUN apt update && apt install gcc build-essential -y && apt clean

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-dev

COPY . .

ENTRYPOINT ["bash"]
CMD ["start.sh"]
