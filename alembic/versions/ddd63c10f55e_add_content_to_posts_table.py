"""add content to posts table

Revision ID: ddd63c10f55e
Revises: 323c61dc8b5c
Create Date: 2022-06-25 05:50:01.779210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddd63c10f55e'
down_revision = '323c61dc8b5c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable =False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
