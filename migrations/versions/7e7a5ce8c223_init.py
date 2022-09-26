"""init

Revision ID: 7e7a5ce8c223
Revises: 
Create Date: 2022-09-25 14:39:39.321529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e7a5ce8c223'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'sample',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),        
    )


def downgrade() -> None:
    op.drop_table('account')
