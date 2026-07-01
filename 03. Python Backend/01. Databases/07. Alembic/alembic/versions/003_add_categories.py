"""add categories table

Revision ID: 003_add_categories
Revises: 002_add_sku
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "003_add_categories"
down_revision: Union[str, None] = "002_add_sku"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=80), nullable=False, unique=True),
    )


def downgrade() -> None:
    op.drop_table("categories")
