"""create posts table

Revision ID: 323c61dc8b5c
Revises: 
Create Date: 2022-06-25 05:41:28.335514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '323c61dc8b5c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.Integer(), nullable=False,primary_key =True),
                            sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
