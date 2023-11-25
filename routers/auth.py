from fastapi import APIRouter, Form
from fastapi.security import OAuth2AuthorizationCodeBearer
from core.config.hashing import PasswordManager

app = APIRouter(
	tags=["Auth"],
	prefix="/auth"
)

@app.get("/login")
async def login():
	pass

routers = [app]