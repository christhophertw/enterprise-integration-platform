import os
import tempfile
from pathlib import Path

# Set before importing application modules.
_tmp = tempfile.TemporaryDirectory()
os.environ["DATABASE_URL"] = f"sqlite:///{Path(_tmp.name) / 'test.db'}"

from fastapi.testclient import TestClient  # noqa: E402
from app.main import app  # noqa: E402


def test_health():
    with TestClient(app) as client:
        assert client.get("/health").json() == {"status": "ok"}


def test_customer_lifecycle():
    with TestClient(app) as client:
        created = client.post("/customers", json={"name": "Example GmbH", "email": "info@example.test"})
        assert created.status_code == 201
        customer_id = created.json()["id"]
        assert client.get(f"/customers/{customer_id}").status_code == 200
        assert any(item["id"] == customer_id for item in client.get("/customers").json())
        assert client.post("/customers", json={"name": "Duplicate", "email": "info@example.test"}).status_code == 409
        assert client.get("/customers/999999").status_code == 404
