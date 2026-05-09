from pydantic import BaseModel


class Address(BaseModel):
    id: int
    street: str
    street_number: int
    city: str
    state: str
    zip_code: str
    neighborhood: str
    zone: str
