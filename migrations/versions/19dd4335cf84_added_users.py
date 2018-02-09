"""Added users

Revision ID: 19dd4335cf84
Revises: 6b78aecc4585
Create Date: 2018-02-09 09:36:51.617764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19dd4335cf84'
down_revision = '6b78aecc4585'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'user_id')
    # ### end Alembic commands ###
