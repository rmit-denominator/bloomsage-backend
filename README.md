# BloomSage Backend

This project uses Python 3.10. Remember to run below commands in the root directory of your project where the `pyproject.toml` file is located. Here are the main elements you need to know to get started:
- Model: 
[rmit-denominator/bloomsage-ml](https://github.com/rmit-denominator/bloomsage-ml.git)

## Virtual Environment
Note that for this the package venv is to be used.

In short, a virtual environment will help us manage an isolated version of python interpreter. And so too installed packages. In this way. Different project will not have to depends on the same packages installation and have to conflict. Read the link above explain and show it well.

## Build on local
### Docker
```docker
# Build the Docker image
docker build -t bloomsage-backend:1.2 .
```
### Python
```bash
# Create a virtual environment, navigate to your root directory and run:
python -m venv .venv
# Activate the environment, use:
source .venv/bin/activate
pip install -r requirements
python ./ml_fetch.py
```

***To add additional dependencies/packages to your project, use:***
```bash
pip install [dependencies/packages]
```

## Local Server
***To start the server at http://0.0.0.0:8000***
### Docker
```bash
# Run the Docker container
docker run --rm -p 8000:8000 bloomsage-backend:1.2
```
### Python
```bash
python ./main.py
```
## Public Server with Ngrok Endpoints
***Make sure that your localhost:8000 is running either by Docker or Python***
### What is ngrok?
ngrok is a globally distributed reverse proxy that secures, protects and accelerates your applications and network services, no matter where you run them.
- See [ngrok Documentation](https://ngrok.com/docs/what-is-ngrok/)
## Once done with the current session
### Docker
```bash
# Stop the Docker container
docker container ls
docker stop <container_id>
```
### Python
```bash
# Snapshot of the project dependencies
pip freeze > requirements.txt

deactivate
```
