# frontend build container
FROM node:19 AS builder

WORKDIR /usr/src/app


COPY frontend/package.json frontend/yarn.lock ./
RUN npm install --prod --frozen-lockfile
COPY frontend ./
RUN npm run build

# application container
FROM python:3.10.7-bullseye

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt /tmp/pip-tmp/
RUN pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp

COPY --from=builder /usr/src/app/build ./static/.
COPY fast_model_db ./fast_model_db/
COPY alembic.ini ./

