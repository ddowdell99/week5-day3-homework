"""empty message

Revision ID: 6ea290e41414
Revises: f82af73ec96a
Create Date: 2022-10-25 20:49:44.282996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ea290e41414'
down_revision = 'f82af73ec96a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('teamTable')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teamTable',
    sa.Column('pokemon_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.pokemon_id'], name='teamTable_pokemon_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], name='teamTable_user_id_fkey')
    )
    op.drop_table('team')
    # ### end Alembic commands ###