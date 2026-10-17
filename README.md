Homelab Status

A containerised Python application built as part of my homelab and DevOps engineering projects.

The application exposes HTTP endpoints that return application status information and a health check. The project will be extended with automated testing, CI/CD, infrastructure automation, and monitoring.

Current Features

* Python application built with Flask.
* JSON responses from the home endpoint.
* Health-check endpoint with a UTC timestamp.
* Docker image built from a lightweight Python base image.
* Gunicorn WSGI server.
* Container runs as a non-root user.
* Automated endpoint tests using pytest.
* Git and Docker ignore rules.

Technology Stack

* Python
* Flask
* Gunicorn
* Docker
* pytest
* Git

API Endpoints

Endpoint	Description
GET /	Returns application information and running status.
GET /health	Returns health status and a UTC timestamp.

Run Locally

Create and activate a Python virtual environment, then install the dependencies:

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Start the application:

python app/main.py

The application listens on port 8000.

Run Tests

Install pytest if necessary:

python -m pip install pytest

Run the tests:

python -m pytest -v

Build and Run with Docker

Build the Docker image:

docker build -t homelab-status:1.0 .

Run the container:

docker run --rm --name homelab-status -p 8000:8000 homelab-status:1.0

Test the endpoints from another terminal:

curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/health

If port 8000 is already in use, stop the existing project container before running another one.

Project Roadmap

* Build the Flask application and health endpoint.
* Add automated endpoint tests.
* Containerise the application with Docker.
* Run the application in a Docker container.
* Publish the source code to GitHub.
* Implement a GitHub Actions CI pipeline.
* Automate Docker image builds.
* Deploy the application to the homelab.
* Explore infrastructure automation and monitoring.

Purpose

This project is a practical environment for developing and demonstrating skills in application testing, containerisation, automation, deployment, and infrastructure operations.