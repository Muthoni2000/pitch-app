"""Dropped schema. Creates db tables
Revision ID: 4624703a098f
Revises: ed3c48d01235
Create Date: 2020-05-04 11:46:16.486371
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4624703a098f'
down_revision = 'ed3c48d01235'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=225), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('bio', sa.String(), nullable=True),
    sa.Column('profile_pic', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitches')
    op.drop_table('users')
    # ### end Alembic commands ###
