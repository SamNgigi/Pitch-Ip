"""Added rest of the object properties to Pitch

Revision ID: 4447a93d59b4
Revises: 186f70eef5df
Create Date: 2018-02-04 17:20:48.111492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4447a93d59b4'
down_revision = '186f70eef5df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('author', sa.String(), nullable=True))
    op.add_column('pitches', sa.Column('body', sa.String(), nullable=True))
    op.add_column('pitches', sa.Column('category', sa.String(), nullable=True))
    op.add_column('pitches', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'title')
    op.drop_column('pitches', 'category')
    op.drop_column('pitches', 'body')
    op.drop_column('pitches', 'author')
    # ### end Alembic commands ###
