"""create drink table

Revision ID: 8a449f1c5a26
Revises: 5e7b30e40037
Create Date: 2022-02-17 18:27:38.405113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a449f1c5a26'
down_revision = '5e7b30e40037'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'drink',
        sa.Column('drink_id', sa.Integer, primary_key=True),
        sa.Column('drink_description', sa.String(45), nullable=False),
    )


def downgrade():
    op.drop_table('drink')
