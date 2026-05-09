from enum import Enum
from pydantic import BaseModel


class UserRole(str, Enum):
    admin = "admin"
    client = "client"


class User(BaseModel):
    id: int
    name: str
    email: str
    role: UserRole
