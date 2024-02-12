from dataclasses import dataclass


@dataclass
class CompanySQLModel:
    table: str = "vt_companies"
    id_col: str = "id"
    name_col: str = "name"
    description_col: str = "description"
