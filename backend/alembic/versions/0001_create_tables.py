from alembic import op
import sqlalchemy as sa

revision = '0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('horses',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False, unique=True),
        sa.Column('owner_id', sa.String(), nullable=True),
        sa.Column('status', sa.String(), nullable=True),
        sa.Column('location', sa.String(), nullable=True),
        sa.Column('breed', sa.String(), nullable=True),
        sa.Column('age', sa.Integer(), nullable=True),
        sa.Column('notes', sa.String(), nullable=True)
    )
    op.create_table('owners',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('name', sa.String()),
        sa.Column('contact_info', sa.String())
    )
    op.create_table('locations',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False, unique=True),
        sa.Column('type', sa.String()),
        sa.Column('capacity', sa.Integer()),
        sa.Column('notes', sa.String())
    )
    op.create_table('races',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False, unique=True),
        sa.Column('date', sa.Date()),
        sa.Column('location', sa.String()),
        sa.Column('notes', sa.String())
    )
    op.create_table('activities',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('horse_id', sa.String(), nullable=False),
        sa.Column('activity_type', sa.String()),
        sa.Column('start_time', sa.DateTime()),
        sa.Column('end_time', sa.DateTime()),
        sa.Column('location', sa.String()),
        sa.Column('notes', sa.String())
    )
    op.create_table('drug_tests',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('horse_id', sa.String()),
        sa.Column('race_id', sa.String()),
        sa.Column('result', sa.String()),
        sa.Column('date', sa.Date()),
        sa.Column('notes', sa.String())
    )
    op.create_table('vet_records',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('horse_id', sa.String()),
        sa.Column('visit_date', sa.Date()),
        sa.Column('notes', sa.String()),
        sa.Column('injury_type', sa.String()),
        sa.Column('treatment', sa.String()),
        sa.Column('follow_up', sa.String())
    )
    op.create_table('race_horses',
        sa.Column('race_id', sa.String(), sa.ForeignKey('races.id')),
        sa.Column('horse_id', sa.String(), sa.ForeignKey('horses.id'))
    )
\n\ndef downgrade():\n    op.drop_table('race_horses')\n    op.drop_table('vet_records')\n    op.drop_table('drug_tests')\n    op.drop_table('activities')\n    op.drop_table('races')\n    op.drop_table('locations')\n    op.drop_table('owners')\n    op.drop_table('horses')
