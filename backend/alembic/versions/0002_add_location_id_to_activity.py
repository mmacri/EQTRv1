from alembic import op
import sqlalchemy as sa

revision = '0002'
down_revision = '0001'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('activities', sa.Column('location_id', sa.String(), sa.ForeignKey('locations.id')))


def downgrade():
    op.drop_column('activities', 'location_id')
