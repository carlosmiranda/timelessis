"""empty message

Revision ID: 1029025e393e
Revises: 9eee25222512
Create Date: 2019-01-28 17:05:56.757201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1029025e393e'
down_revision = '49f5103c70fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scheme_types',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('default_value', sa.String(), nullable=False),
    sa.Column('value_type', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description')
    )
    op.add_column('scheme_conditions', sa.Column('scheme_type_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'scheme_conditions', 'scheme_types', ['scheme_type_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'scheme_conditions', type_='foreignkey')
    op.drop_column('scheme_conditions', 'scheme_type_id')
    op.drop_table('scheme_types')
    # ### end Alembic commands ###
