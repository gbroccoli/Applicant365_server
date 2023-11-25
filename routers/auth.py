from fastapi import APIRouter, Form
from fastapi.security import OAuth2AuthorizationCodeBearer
from core.config.hashing import PasswordManager
from pydantic import BaseModel, Field
from typing import Optional
import random

class User(BaseModel):
	id: Optional[int] = None
	surname: str
	name: str
	login: str
	passwd: str

fake_bd = []

app = APIRouter(
	tags=["Auth"],
	prefix="/auth"
)

@app.get("/login")
async def login():
	pass

@app.post("/gets")
async def hash(password: str = Form(...)):
	return PasswordManager.hash_password(password)

@app.post("/register")
async def register(item: User):
	return item

routers = [app]