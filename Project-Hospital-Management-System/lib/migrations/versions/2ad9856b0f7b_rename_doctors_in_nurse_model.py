"""Rename doctors in Nurse model

Revision ID: 2ad9856b0f7b
Revises: 18ed8205f857
Create Date: 2023-10-05 14:06:25.803705

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ad9856b0f7b'
down_revision: Union[str, None] = '18ed8205f857'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###