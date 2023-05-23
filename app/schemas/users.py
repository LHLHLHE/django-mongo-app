from pydantic import BaseModel, EmailStr


class Customer(BaseModel):
    id: int
    email: EmailStr
    password: str


class Employee(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: str
    phone_number: str
    department_name: str
    schedule: str
