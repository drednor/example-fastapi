"""add foreign key to posts table

Revision ID: b835e3feaeb1
Revises: 84315db116c6
Create Date: 2022-06-25 06:01:49.311176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b835e3feaeb1'
down_revision = '84315db116c6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable =False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users',
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name= "posts")
    op.drop_column('posts','owner_id')
    pass
