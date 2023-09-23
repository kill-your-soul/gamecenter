FROM python:3.10 as builder

WORKDIR /build

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM python:3.10-slim-buster

WORKDIR /app
RUN apt-get update && \
    apt-get install -y libpq-dev
RUN mkdir -p /home/app
COPY --from=builder /build/wheels /app/wheels
COPY --from=builder /build/requirements.txt .
RUN pip install --upgrade pip 
RUN pip install --no-cache /app/wheels/*