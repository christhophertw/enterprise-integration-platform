# Development Log

## v0.1.0 — Initial scaffold
- Created FastAPI backend with health and customer CRUD subset (create/list/get).
- Added SQLAlchemy models and PostgreSQL Compose service.
- Added initial tests, documentation, and example environment settings.
- Deployment and test execution on the user's Windows machine remain to be verified.
- Next: validate locally, add CI, migrations, customer updates, and ERP domain entities.

## v0.1.1 — Local verification and CI
- Confirmed Docker Compose starts PostgreSQL (healthy) and FastAPI on Windows.
- Verified customer creation and retrieval through Swagger UI.
- Diagnosed missing pytest in the production API image; added a dedicated test image and Compose override.
- Ran the isolated test container: 2 passed, 1 dependency deprecation warning.
- Confirmed existing pytest suite overrides DATABASE_URL to a temporary SQLite file; it does not use the development PostgreSQL database.
- Added GitHub Actions workflow to run backend pytest on pushes to main/ci branches and pull requests targeting main.
- CI workflow results must be verified in GitHub Actions after pushing.
- Next: evaluate PostgreSQL integration tests, migrations, and additional ERP entities.

## v0.2.0 — Product catalog (proposed)
- Added Product ORM entity, validated request/response schemas, and create/list/get endpoints.
- Added tests for product creation, retrieval, SKU normalization, duplicate prevention, and invalid pricing.
- Product is independent of customers and stock balances; see ADR-006.
- CI validation pending; do not merge until GitHub Actions passes.
- Schema creation still uses MVP create_all; Alembic migrations remain planned before production.
