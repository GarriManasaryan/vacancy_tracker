"""locations

Revision ID: bd99d6618e9a
Revises: fdee3a5f1403
Create Date: 2024-02-18 00:21:59.896175

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bd99d6618e9a"
down_revision = "fdee3a5f1403"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        """create table vacancy_tracker.public.vt_locations(
            id varchar(64) not null,
            country varchar(512) not null,
            state varchar(512),
            city varchar(512) not null,
            primary key(id)
        );
        """
    )


def downgrade() -> None:
    op.execute(
        """
        drop table vacancy_tracker.public.vt_locations;
        """
    )
