from dataclasses import dataclass
from typing import Optional


@dataclass
class SalarySQLModel:
    table: str = "vt_salaries"
    id_col: str = "id"
    min_col: str = "min"
    max_col: str = "max"
