"""create research table

Revision ID: b6d9d367c6c0
Revises: 03a74d37fab9
Create Date: 2022-02-17 18:28:33.276958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6d9d367c6c0'
down_revision = '03a74d37fab9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'research',
        sa.Column('research_id', sa.Integer, primary_key=True),
        sa.Column('research_date', sa.Date, nullable=False),
        sa.Column('person_id', sa.Integer, sa.ForeignKey('person.person_id'), nullable=False),
        sa.Column('pet_id', sa.Integer, sa.ForeignKey('pet.pet_id'), nullable=False),
        sa.Column('drink_id', sa.Integer, sa.ForeignKey('drink.drink_id'), nullable=False),
        sa.Column('hobby_id', sa.Integer, sa.ForeignKey('hobby.hobby_id'), nullable=False),
        sa.Column('weather_id', sa.Integer, sa.ForeignKey('weather.weather_id'), nullable=False),
    )


def downgrade():
    op.drop_table('research')
