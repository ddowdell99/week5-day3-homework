"""empty message

Revision ID: 92719c9be921
Revises: 24b19f2bc4dd
Create Date: 2022-10-26 21:44:08.226472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92719c9be921'
down_revision = '24b19f2bc4dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('wins', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('losses', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('ties', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'ties')
    op.drop_column('user', 'losses')
    op.drop_column('user', 'wins')
    # ### end Alembic commands ###