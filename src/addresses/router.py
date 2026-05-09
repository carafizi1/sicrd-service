from fastapi import APIRouter, HTTPException
from .models import Address

router = APIRouter(prefix="/address")

addresses: list[Address] = [
    Address(id=1, street="Rua da Mangueira", street_number=52, city="Fortaleza", state="CE", zip_code="60352-630", neighborhood="Quintino Cunha", zone="Residencial"),
    Address(id=2, street="Rua da Águia", street_number=322, city="Natal", state="RN", zip_code="59125-375", neighborhood="Pajuçara", zone="Hospitalar"),
]


@router.get("/")
def get_addresses() -> list[Address]:
    return addresses


@router.get("/{address_id}")
def get_address(address_id: int) -> Address:
    for address in addresses:
        if address.id == address_id:
            return address
    raise HTTPException(status_code=404, detail="Address not found")


@router.post("/")
def create_address(address: Address) -> Address:
    addresses.append(address)
    return address


@router.delete("/{address_id}")
def delete_address(address_id: int) -> dict:
    for address in addresses:
        if address.id == address_id:
            addresses.remove(address)
            return {"deleted": address_id}
    raise HTTPException(status_code=404, detail="Address not found")
