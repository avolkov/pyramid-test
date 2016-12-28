"""Initial migration

Revision ID: af77678bd821
Revises:
Create Date: 2016-12-28 16:32:16.913239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af77678bd821'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'models',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Text),
        sa.column('value', sa.Integer)
    )

