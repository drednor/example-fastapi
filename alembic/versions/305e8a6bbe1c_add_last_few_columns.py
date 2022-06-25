"""add last few columns

Revision ID: 305e8a6bbe1c
Revises: b835e3feaeb1
Create Date: 2022-06-25 06:09:03.032734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '305e8a6bbe1c'
down_revision = 'b835e3feaeb1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='True'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
