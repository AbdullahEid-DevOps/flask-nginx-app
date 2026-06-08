# Flask + PostgreSQL + Nginx - Multi-Container App

A multi-container application built with Docker Compose, demonstrating container orchestration, networking, and data persistence.

## Architecture

Browser -> Nginx (port 80) -> Flask (port 5000) -> PostgreSQL (port 5432)

## Stack

- Flask - Python web framework
- PostgreSQL - relational database
- Nginx - reverse proxy
- Docker Compose - container orchestration

## How to Run

docker compose up -d

Then visit:
- http://localhost - home page
- http://localhost/db - database connection test

## Concepts Demonstrated

- Multi-service Docker Compose setup
- Container networking via service name resolution
- Data persistence with named volumes
- Reverse proxy configuration with Nginx
- Environment variable injection
