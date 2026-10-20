from decimal import Decimal

from fastapi.testclient import TestClient

from app.main import app


def test_product_lifecycle():
    with TestClient(app) as client:
        created = client.post(
            "/products",
            json={"sku": " prd-001 ", "name": " Example Item ", "price": "19.90"},
        )
        assert created.status_code == 201, created.text
        product = created.json()
        assert product["sku"] == "PRD-001"
        assert product["name"] == "Example Item"
        assert Decimal(str(product["price"])) == Decimal("19.90")
        assert product["active"] is True

        product_id = product["id"]
        assert client.get(f"/products/{product_id}").json()["sku"] == "PRD-001"
        assert any(item["id"] == product_id for item in client.get("/products").json())
        assert client.get("/products/999999").status_code == 404


def test_product_validation_and_duplicate_sku():
    with TestClient(app) as client:
        assert client.post(
            "/products",
            json={"sku": "  ", "name": "Item", "price": "1.00"},
        ).status_code == 422
        assert client.post(
            "/products",
            json={"sku": "NEG-001", "name": "Item", "price": "-1.00"},
        ).status_code == 422
        assert client.post(
            "/products",
            json={"sku": "PREC-001", "name": "Item", "price": "1.999"},
        ).status_code == 422
        assert client.post(
            "/products",
            json={"sku": "DUP-001", "name": "First", "price": "1.00"},
        ).status_code == 201
        assert client.post(
            "/products",
            json={"sku": "dup-001", "name": "Second", "price": "2.00"},
        ).status_code == 409
