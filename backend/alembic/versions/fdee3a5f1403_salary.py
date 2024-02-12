"""salary

Revision ID: fdee3a5f1403
Revises: a7557852100a
Create Date: 2024-02-12 22:01:28.063928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdee3a5f1403'
down_revision = 'a7557852100a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        '''create table vacancy_tracker.public.vt_salaries(
            id varchar(64) not null,
            min integer,
            max integer,
            primary key(id)
        );
        '''
    )


def downgrade() -> None:
    op.execute(
        '''
        drop table vacancy_tracker.public.vt_salaries;
        '''
    )
