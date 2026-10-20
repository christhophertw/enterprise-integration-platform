# Architecture Decision Records

## ADR-001 — FastAPI for the HTTP backend
**Status:** Accepted (MVP)
**Context:** An integration-focused application needs typed REST endpoints and accessible API documentation.
**Decision:** Use FastAPI and Pydantic.
**Alternatives:** Flask, Django REST Framework.
**Trade-offs:** Lightweight and explicit, but authentication, persistence patterns and operational concerns require deliberate implementation.

## ADR-002 — PostgreSQL for persistent storage
**Status:** Accepted
**Context:** Customers and future orders require relational consistency and constraints.
**Decision:** PostgreSQL with SQLAlchemy ORM.
**Alternatives:** SQLite, MySQL.
**Trade-offs:** PostgreSQL is production-relevant but requires a database service; SQLite is used only for quick isolated tests.

## ADR-003 — Docker Compose for local orchestration
**Status:** Accepted
**Decision:** Compose starts FastAPI and PostgreSQL with health-based startup dependency.
**Trade-offs:** Reproducible local setup; not by itself a production orchestration strategy.

## ADR-004 — MVP schema bootstrap
**Status:** Temporary
**Decision:** SQLAlchemy `create_all()` initializes the database in v0.1.0.
**Trade-offs:** Simple first run; it cannot manage schema changes. Replace with Alembic migrations before production.

## ADR-005 — Simple module boundaries first
**Status:** Accepted
**Decision:** Separate HTTP handlers, persistence models, schemas and DB setup without premature microservices.
**Trade-offs:** Faster iteration; introduce services and repositories as business complexity justifies them.

## ADR-006 — Independent product master data
**Status:** Accepted (v0.2)
**Context:** Products must exist independently of customers, sales/purchase orders, and inventory transactions.
**Decision:** Introduce a Product entity with unique normalized SKU, name, nonnegative decimal reference price, and active flag. Do not store stock balance on Product.
**Trade-offs:** Simple MVP catalog; currency, price lists, units of measure, warehouses, and inventory movements will be modeled separately in later iterations. SKU normalization to uppercase is an explicit API policy.
