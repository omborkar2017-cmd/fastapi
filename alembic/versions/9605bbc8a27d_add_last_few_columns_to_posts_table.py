"""add last few columns to posts table

Revision ID: 9605bbc8a27d
Revises: 6d12a0a79c19
Create Date: 2026-11-01 14:25:58.105677

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9605bbc8a27d'
down_revision: Union[str, Sequence[str], None] = '6d12a0a79c19'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
