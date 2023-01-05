FROM python:3.10.9-bullseye

ENV POETRY_VERSION=1.2.2

WORKDIR /app
EXPOSE 8000
RUN pip install "poetry==$POETRY_VERSION"
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

COPY . /app
CMD gunicorn -b 0.0.0.0 app:app
