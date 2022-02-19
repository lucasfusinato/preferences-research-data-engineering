"""create hobby table

Revision ID: a0f177ea45ae
Revises: 2eb92cc2bcc2
Create Date: 2022-02-17 18:28:11.716024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0f177ea45ae'
down_revision = '2eb92cc2bcc2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'hobby',
        sa.Column('hobby_id', sa.Integer, primary_key=True),
        sa.Column('hobby_description', sa.String(45), nullable=False)
    )


def downgrade():
    op.drop_table('hobby')
