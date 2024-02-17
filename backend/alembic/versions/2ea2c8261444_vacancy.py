"""vacancy

Revision ID: 2ea2c8261444
Revises: bd99d6618e9a
Create Date: 2024-02-18 01:08:13.015946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ea2c8261444'
down_revision = 'bd99d6618e9a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        """create table vacancy_tracker.public.vt_vacancies(
            id varchar(64) not null,
            title text not null,
            description text not null,
            company_id varchar(64) not null,
            salary_id varchar(64),
            location_id varchar(64),
            url text not null,
            submitted_at timestamp with time zone,
            primary key(id),
            constraint fk_vacancies_salary_id foreign key (salary_id) references vt_salaries(id),
            constraint fk_vacancies_company_id foreign key (company_id) references vt_companies(id),
            constraint fk_vacancies_location_id foreign key (location_id) references vt_locations(id)
        );
        """
    )


def downgrade() -> None:
    op.execute(
        """
        drop table vacancy_tracker.public.vt_vacancies;
        """
    )