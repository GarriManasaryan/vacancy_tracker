from pydantic import BaseModel


class RequirementsCreationRequest(BaseModel):
    name: str


class RequirementsBackofficeModel(BaseModel):
    id: str
    name: str
