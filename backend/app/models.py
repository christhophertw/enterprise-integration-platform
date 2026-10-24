from decimal import Decimal

from sqlalchemy import Boolean, Numeric, String
from sqlalchemy import (
    ForeignKeyConstraint,
    UniqueConstraint,
    CheckConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    sku: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)


class Warehouse(Base):
    __tablename__ = "warehouses"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)


class StockBalance(Base):
    __tablename__ = "stock_balances"
    __table_args__ = (
        ForeignKeyConstraint(["product_id"], ["products.id"]),
        ForeignKeyConstraint(["warehouse_id"], ["warehouses.id"]),
        UniqueConstraint("product_id", "warehouse_id", name="uq_product_id_warehouse-id"),
        CheckConstraint(
            "quantity >= 0",
            name="ck_stock_balance_nonnegative"
        )
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(nullable=False)
    warehouse_id: Mapped[int] = mapped_column(nullable=False)
    quantity: Mapped[Decimal] = mapped_column(Numeric(18, 3), nullable=False)