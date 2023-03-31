FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    git \
    nano \
    tzdata

ADD backend/requirements.txt /requirements/backend.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r /requirements/backend.txt

ADD db/requirements.txt /requirements/db.txt
RUN pip install --no-cache-dir --upgrade -r /requirements/db.txt

ADD redis/py/requirements.txt /requirements/redis.txt
RUN pip install --no-cache-dir --upgrade -r /requirements/redis.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
