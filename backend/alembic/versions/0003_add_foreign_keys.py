from alembic import op
import sqlalchemy as sa

revision = '0003'
down_revision = '0002'
branch_labels = None
depends_on = None


def upgrade():
    op.create_foreign_key('fk_horses_owner_id', 'horses', 'owners', ['owner_id'], ['id'])
    op.create_foreign_key('fk_activities_horse_id', 'activities', 'horses', ['horse_id'], ['id'])
    op.create_foreign_key('fk_drug_tests_horse_id', 'drug_tests', 'horses', ['horse_id'], ['id'])
    op.create_foreign_key('fk_drug_tests_race_id', 'drug_tests', 'races', ['race_id'], ['id'])
    op.create_foreign_key('fk_vet_records_horse_id', 'vet_records', 'horses', ['horse_id'], ['id'])


def downgrade():
    op.drop_constraint('fk_vet_records_horse_id', 'vet_records', type_='foreignkey')
    op.drop_constraint('fk_drug_tests_race_id', 'drug_tests', type_='foreignkey')
    op.drop_constraint('fk_drug_tests_horse_id', 'drug_tests', type_='foreignkey')
    op.drop_constraint('fk_activities_horse_id', 'activities', type_='foreignkey')
    op.drop_constraint('fk_horses_owner_id', 'horses', type_='foreignkey')
