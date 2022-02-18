"""create weather table

Revision ID: 2eb92cc2bcc2
Revises: 8a449f1c5a26
Create Date: 2022-02-17 18:27:59.550960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2eb92cc2bcc2'
down_revision = '8a449f1c5a26'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'weather',
        sa.Column('weather_id', sa.Integer, primary_key=True),
        sa.Column('weather_description', sa.String(45), nullable=False),
    )


def downgrade():
    op.drop_table('weather')
