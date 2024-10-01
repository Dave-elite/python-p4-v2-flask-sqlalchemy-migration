"""Add address column to departments

Revision ID: f1135e4393e4
Revises: d4ffa183b335
Create Date: 2024-10-01 12:54:59.085749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1135e4393e4'
down_revision = 'd4ffa183b335'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('departments', sa.Column('address', sa.String(), nullable=True))

def downgrade():
    op.drop_column('departments', 'address')

