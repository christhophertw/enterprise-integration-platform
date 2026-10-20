# Architecture

## v0.1.0
Client (Swagger UI / HTTP) -> FastAPI -> SQLAlchemy -> PostgreSQL.
Docker Compose starts the API and database. Only the API is bound to the host loopback address (`127.0.0.1:8000`); PostgreSQL is private to the Compose network.

## Boundaries
- API: HTTP validation, status codes and orchestration.
- Models: persistence schema.
- Schemas: input/output contracts.
- Database: SQLAlchemy engine and session lifecycle.

## Next evolution
Extract repository/service layers when domain rules grow; introduce Alembic migrations, auth, integration adapters, async event processing and Angular. Do not share databases between future services.
