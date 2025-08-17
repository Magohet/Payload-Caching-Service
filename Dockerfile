FROM python:3.13.4-slim-bookworm

WORKDIR /opt

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD uvicorn config.app:app --host $APP_HOST --port $APP_PORT --workers $APP_WORKERS --log-level debug
