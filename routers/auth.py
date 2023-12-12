from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2AuthorizationCodeBearer
from core.config.hashing import PasswordManager
from core.config.datebase import async_session_maker
from pydantic import BaseModel, Field
from typing import Optional
import logging
from core.features.datadase import DatabaseCRUD

logger = logging.getLogger(__name__)


class Nominee(BaseModel):
	surname: str
	name: str
	patronymic: Optional[str] = None
	login: str
	passwd: str


fake_bd = []

app = APIRouter(
	tags=["Auth"],
	prefix="/auth"
)


# @app.get("/login")
# async def login(user: User, request: Request):
# 	return user


@app.post("/gets")
async def hash(password: str = Form(...)):
	logger.error("Creating hash from password")
	return PasswordManager.hash_password(password)

@app.post("/verify_password")
async def verify_password(password: str = Form(...)):
	return PasswordManager.verify_password(password, PasswordManager.hash_password(password))

@app.post("/register")
async def register(nominee: Nominee):

	if len(nominee.surname) == 0 or len(nominee.name) == 0 or len(nominee.login) == 0 or len(nominee.passwd) == 0:
		return JSONResponse(status_code=400, content={"error" : "Часть данных нету"})

	passwd = nominee.passwd

	if len(passwd) < 8:
		return JSONResponse(status_code=400, content={"error" : "Пароль не соотвествует требованиям"})

	passwd = PasswordManager.hash_password(passwd)

	result = await DatabaseCRUD.selectDB(query="SELECT login FROM users WHERE login = :login", data={
		"login" : nominee.login
	})

	if result:
		return JSONResponse(status_code=400, content={"error" : "Данный пользователь уже существует" })
	
	await DatabaseCRUD.insertDB(query="INSERT INTO users (surname, name, patronymic, login, passwd) VALUES (:surname, :name, :patronymic, :login, :passwd)", data={"surname": nominee.surname,"name": nominee.name,"patronymic": nominee.patronymic,"login": nominee.login,"passwd": passwd})

	return JSONResponse(status_code=201, content={"success" : "ok"})
	
routers = [app]
