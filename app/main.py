from datetime import date
from enum import Enum
from json import dumps
from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, field_validator


class Department(Enum):
    HR = "HR"
    SALES = "SALES"
    IT = "IT"
    ENGINEERING = "ENGINEERING"


class Employee(BaseModel):
    employee_id: UUID = uuid4()
    name: str
    email: EmailStr
    date_of_birth: date
    salary: float
    department: Department
    elected_benefits: bool

    @field_validator("salary")
    def salary_must_be_small(value):
        if value > 150000:
            raise ValueError("Произошло раскулачивание")
        return value


person = Employee(
    employee_id=uuid4(),
    name="John Doe",
    email="a@pussy.cum",
    date_of_birth="2001-05-20",
    salary=100000,
    department="HR",
    elected_benefits=False,
)

# print(person.model_dump())
# print()
print(Employee.model_json_schema())
print()
