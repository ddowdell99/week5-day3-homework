"""empty message

Revision ID: 051bfe27515b
Revises: 850b02d29c7b
Create Date: 2022-10-26 21:57:21.612676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '051bfe27515b'
down_revision = '850b02d29c7b'
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
