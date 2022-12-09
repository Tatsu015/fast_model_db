"""modify table name

Revision ID: 4a81f6d30f77
Revises: 7e7a5ce8c223
Create Date: 2022-12-09 22:17:38.822636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a81f6d30f77'
down_revision = '7e7a5ce8c223'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),        
    )


def downgrade() -> None:
    op.drop_table('users')
