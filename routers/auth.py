from fastapi import APIRouter, Form
from fastapi.security import OAuth2AuthorizationCodeBearer
from core.config.hashing import PasswordManager
from pydantic import BaseModel, Field
from typing import Optional
import logging

logger = logging.getLogger(__name__)


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
	logger.error("Creating hash from password")
	return PasswordManager.hash_password(password)

@app.post("/verify_password")
async def verify_password(password: str = Form(...)):
	return PasswordManager.verify_password(password, PasswordManager.hash_password(password))

# @app.post("/register")
# async def register(surname: str = Form(...), name: str = Form(...), login: str = Form(...), password: str = Form(...)):
# 	new_id = random.randint(1, 100)
# 	new_user = {
# 		"id": new_id,
# 		"surname": surname,
# 		"name": name,
# 		"login": login,
# 		"password": PasswordManager.hash_password(password)
# 	}

# 	fake_bd.append(new_user)  # Добавляем нового пользователя в список

# 	return fake_bd  # Возвращаем только что добавленного пользователя

routers = [app]
