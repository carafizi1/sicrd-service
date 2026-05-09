from fastapi import APIRouter, HTTPException
from .models import User, UserRole

router = APIRouter(prefix="/users")

users: list[User] = [
    User(id=1, name="Pedro", email="pedro@dominio.com", role=UserRole.admin),
    User(id=2, name="Gabriel", email="gabriel@carafizi.com", role=UserRole.client),
]


@router.get("/")
def get_users() -> list[User]:
    return users


@router.get("/{user_id}")
def get_user(user_id: int) -> User:
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.post("/")
def create_user(user: User) -> User:
    users.append(user)
    return user


@router.delete("/{user_id}")
def delete_user(user_id: int) -> dict:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"deleted": user_id}
    raise HTTPException(status_code=404, detail="User not found")
