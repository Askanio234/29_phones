"""add normal_phones column

Revision ID: 2e668acbbea3
Revises: 
Create Date: 2017-06-27 22:37:34.771806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e668acbbea3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('orders', sa.Column('normal_phones', sa.VARCHAR(length=120)))


def downgrade():
    op.drop_column('orders', 'normal_phones')
