FROM python:3.13-slim

RUN apt-get update && apt-get install -yqq make && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN uv venv --allow-existing /opt/venv --python 3.13

WORKDIR /project

RUN mkdir /project/code

COPY . .

CMD ["make", "test"]
