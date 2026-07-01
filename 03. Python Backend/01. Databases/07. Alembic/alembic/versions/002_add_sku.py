"""add sku column to products

Revision ID: 002_add_sku
Revises: 001_initial
Create Date: 2026-07-01
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "002_add_sku"
down_revision: Union[str, None] = "001_initial"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("products", sa.Column("sku", sa.String(length=50), nullable=True))


def downgrade() -> None:
    op.drop_column("products", "sku")
