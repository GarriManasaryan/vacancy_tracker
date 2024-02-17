from fastapi import Depends, Header, HTTPException, Request

from port.adapters.backoffice.salary_model import SalaryCreationRequest


def validate_salary_creation_request(
    creation_request: SalaryCreationRequest,
) -> SalaryCreationRequest:
    if creation_request.min is None and creation_request.max is None:
        raise HTTPException(
            status_code=404, detail="Both min and max values cant be empty"
        )
    return creation_request


def validate_vacancy_creation_request(
        creation_request: SalaryCreationRequest,
) -> SalaryCreationRequest:
    if creation_request.min is None and creation_request.max is None:
        raise HTTPException(
            status_code=404, detail="Both min and max values cant be empty"
        )
    return creation_request
