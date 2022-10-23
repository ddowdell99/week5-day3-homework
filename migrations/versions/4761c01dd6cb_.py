"""empty message

Revision ID: 4761c01dd6cb
Revises: 
Create Date: 2022-10-22 21:43:29.708778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4761c01dd6cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('pokemon_img', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('ability', sa.String(length=50), nullable=False),
    sa.Column('attack', sa.Integer(), nullable=False),
    sa.Column('hp', sa.Integer(), nullable=False),
    sa.Column('defense', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('pokemon_id')
    )
    op.create_table('team_pokemon_join',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('team',
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('team_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('team')
    op.drop_table('user')
    op.drop_table('team_pokemon_join')
    op.drop_table('pokemon')
    # ### end Alembic commands ###
