"""create pet table

Revision ID: 5e7b30e40037
Revises: 
Create Date: 2022-02-17 18:27:22.557285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e7b30e40037'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'pet',
        sa.Column('pet_id', sa.Integer, primary_key=True),
        sa.Column('pet_animal', sa.String(45), nullable=False),
    )


def downgrade():
    op.drop_table('pet')
