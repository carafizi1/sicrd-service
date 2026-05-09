from fastapi import FastAPI
from .users.router import router as users_router
from .addresses.router import router as addresses_router

app = FastAPI()

app.include_router(users_router)
app.include_router(addresses_router)
