# syntax=docker/dockerfile:1.4

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/
FROM --platform=$BUILDPLATFORM tensorflow/tensorflow:latest

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN python -m pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install --timeout=2000 -r requirements.txt

# Copy the source code into the container.
COPY . .

# Initialize the model and dataset
RUN python ml_fetch.py

# Expose the port that the application listens on.
EXPOSE 8000/tcp

# Run the application.
CMD uvicorn 'main:app' --host=0.0.0.0 --port=8000
