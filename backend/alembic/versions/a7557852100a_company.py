"""company

Revision ID: a7557852100a
Revises: 5f17cec09373
Create Date: 2024-02-12 05:47:02.837636

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a7557852100a"
down_revision = "5f17cec09373"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        """create table vacancy_tracker.public.vt_companies(
            id varchar(64) not null,
            name varchar(256) not null,
            description text,
            primary key(id)
        );
        """
    )


def downgrade() -> None:
    op.execute(
        """
        drop table vacancy_tracker.public.vt_companies;
        """
    )
