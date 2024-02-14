from fastapi import APIRouter

from port.adapters.backoffice.resource.company import CompanyController
from port.adapters.backoffice.resource.requirement import RequirementsController
from port.adapters.backoffice.resource.salary import SalaryController
from port.adapters.persistence.postgresql_company_repo import PostgreSQLCompanyRepo
from port.adapters.persistence.postgresql_requirements_repo import (
    PostgreSQLRequirementsRepo,
)
from port.adapters.persistence.postgresql_salary_repo import PostgreSQLSalaryRepo

project_route = APIRouter(prefix="/api")  # tags для доков

requirements = RequirementsController(repository=PostgreSQLRequirementsRepo())
companies = CompanyController(repository=PostgreSQLCompanyRepo())
salaries = SalaryController(repository=PostgreSQLSalaryRepo())

project_route.add_api_route(
    "/company",
    companies.all,
    methods=["GET"],
    tags=["company"],
)
project_route.add_api_route(
    "/company",
    companies.save,
    methods=["POST"],
    tags=["company"],
)
project_route.add_api_route(
    "/requirements",
    requirements.all,
    methods=["GET"],
    tags=["requirements"],
)
project_route.add_api_route(
    "/requirements",
    requirements.save,
    methods=["POST"],
    tags=["requirements"],
)
project_route.add_api_route(
    "/salaries",
    salaries.all,
    methods=["GET"],
    tags=["salaries"],
)
project_route.add_api_route(
    "/salaries",
    salaries.save,
    methods=["POST"],
    tags=["salaries"],
)
