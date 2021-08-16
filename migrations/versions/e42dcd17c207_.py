"""empty message

Revision ID: e42dcd17c207
Revises: 3e667bc3ff4b
Create Date: 2021-08-16 21:38:48.794198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e42dcd17c207'
down_revision = '3e667bc3ff4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('measure',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('cat_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cat_id'], ['cat.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_measure_timestamp'), 'measure', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_measure_timestamp'), table_name='measure')
    op.drop_table('measure')
    # ### end Alembic commands ###
