from pydantic import BaseModel


class Requirement(BaseModel):
    id: str
    name: str
