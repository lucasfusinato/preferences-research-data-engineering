"""create person table

Revision ID: 03a74d37fab9
Revises: a0f177ea45ae
Create Date: 2022-02-17 18:28:17.056131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03a74d37fab9'
down_revision = 'a0f177ea45ae'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'person',
        sa.Column('person_id', sa.Integer, primary_key=True),
        sa.Column('person_gender', sa.String(45), nullable=False),
        sa.Column('person_birthdate', sa.String(45), nullable=False),
    )


def downgrade():
    op.drop_table('person')
