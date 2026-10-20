# Enterprise Integration Platform

Portfolio project: an enterprise integration ecosystem built incrementally with Python, FastAPI, PostgreSQL, Docker, and later Angular, automation, and data pipelines.

## MVP v0.1.0
- `GET /health`
- `POST /customers`
- `GET /customers`
- `GET /customers/{id}`
- PostgreSQL storage and Docker Compose local deployment
- Automated API tests using SQLite as a lightweight test database

## Prerequisites
Docker Desktop with Docker Compose; Git for version control.

## Start locally (PowerShell)
```powershell
Copy-Item .env.example .env
docker compose up -d --build
docker compose ps
```
Open http://localhost:8000/docs for interactive API documentation.

Try a customer:
```powershell
Invoke-RestMethod -Method Post -Uri http://localhost:8000/customers -ContentType 'application/json' -Body '{"name":"Example GmbH","email":"info@example.test"}'
Invoke-RestMethod -Uri http://localhost:8000/customers
```

Stop containers (preserve database):
```powershell
docker compose down
```
**Warning:** `docker compose down -v` deletes the PostgreSQL volume and its data.

## Tests
The runtime Docker image does not contain test dependencies or test files. Run the tests in an ephemeral Python container:
```powershell
docker run --rm -v "${PWD}/backend:/code" -w /code python:3.12-slim sh -c "pip install -r requirements-dev.txt && pytest -q"
```

## Project documentation
- `docs/ARCHITECTURE.md` — components and boundaries
- `docs/DECISIONS.md` — architectural decisions and trade-offs
- `docs/DEVELOPMENT_LOG.md` — implementation history
- `docs/ROADMAP.md` — planned milestones

## Scope and security
This is an educational MVP, **not production ready**. It lacks authentication, authorization, rate limiting, production migrations, observability, and hardened deployment settings. Do not put real customer data or credentials in the repository. `.env` is ignored by Git.
