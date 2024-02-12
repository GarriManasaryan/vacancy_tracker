from dataclasses import dataclass


@dataclass
class RequirementSQLModel:
    table: str = "vt_requirements"
    id_col: str = "id"
    name_col: str = "name"


if __name__ == '__main__':
    print(RequirementSQLModel.table)
