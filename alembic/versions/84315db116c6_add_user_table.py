"""add user table

Revision ID: 84315db116c6
Revises: ddd63c10f55e
Create Date: 2022-06-25 05:54:16.654333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84315db116c6'
down_revision = 'ddd63c10f55e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                              sa.PrimaryKeyConstraint('id'),
                              sa.UniqueConstraint('email')
                              )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
