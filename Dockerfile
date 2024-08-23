FROM python:3.12.4-slim

# ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV} \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    DJANGO_SECRET_KEY='devsecretkey'

RUN apt update && \
    apt install --no-install-recommends -y curl build-essential git locales-all wait-for-it

RUN curl -sSL https://install.python-poetry.org | python3 -

RUN pip install --no-cache-dir --upgrade pip uwsgi

WORKDIR /app

ADD pyproject.toml /app
# RUN poetry install $(test "$YOUR_ENV" == production && echo "--only=main") --no-interaction --no-ansi
RUN poetry install --no-root --no-interaction --no-ansi

COPY . /app

# RUN ./manage.py collectstatic --no-input

# # CMD ./manage.py migrate && uwsgi --master --http :8000 --module app.wsgi
 