from fastapi import APIRouter, Form, status, Response, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2AuthorizationCodeBearer
from core.config.hashing import PasswordManager
from core.config.datebase import async_session_maker
from pydantic import BaseModel
from typing import Optional
import logging
from core.features.datadase import DatabaseCRUD
from core.features.password import ValidationPassword
from core.features.jwt import Token
from core.config.config import EnvVariables

logger = logging.getLogger(__name__)

TypeZone = EnvVariables().get_value("APP_UTC")

class Nominee(BaseModel):
	surname: str
	name: str
	patronymic: Optional[str] = None
	login: str
	passwd: str

class User(BaseModel):
	login: str
	passwd: str
	remember: Optional[bool] = False

app = APIRouter(
	tags=["Auth"],
	prefix="/auth"
)

@app.post("/login")
async def login(user: User, response: Response, request: Request):

	if not (user.login and user.passwd):
		return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"error" : "Не все обязательные данные указаны"})
	
	userCVari = await DatabaseCRUD.selectDB_one(query="SELECT id, login, passwd FROM users WHERE login = :login", data={"login": user.login})

	if not userCVari:
		raise JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"error": "User not found"})

	id, login, passwd = userCVari

	if not PasswordManager.verify_password(user.passwd, passwd):
		return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"error": "Invalid login or password"})
	
	access_token = Token.create({"us": id}, user.remember)

	response.set_cookie(
		key="access_token",
		value=access_token,
		httponly=True,
		max_age=30*24*60*60 if user.remember else 7200,
		expires=30*24*60*60 if user.remember else 7200		
	)

	return {"message": "Logged in successfully"}

@app.post("/register")
async def register(nominee: Nominee):

	if not (nominee.surname and nominee.name and nominee.login and nominee.passwd):
		return JSONResponse(status_code=400, content={"error" : "Не все обязательные данные указаны"})

	passwd = nominee.passwd
	if not ValidationPassword.is_valid_password(password=passwd):
		return JSONResponse(status_code=400, content={"error" : "Пароль не соответствует требованиям"})

	result = await DatabaseCRUD.selectDB(query="SELECT login FROM users WHERE login = :login", data={"login" : nominee.login})
	if result:
		return JSONResponse(status_code=400, content={"error" : "Данный пользователь уже существует" })

	passwd = PasswordManager.hash_password(passwd)
	await DatabaseCRUD.insertDB(query="INSERT INTO users (surname, name, patronymic, login, passwd) VALUES (:surname, :name, :patronymic, :login, :passwd)", data={"surname": nominee.surname,"name": nominee.name,"patronymic": nominee.patronymic,"login": nominee.login,"passwd": passwd})

	return JSONResponse(status_code=201, content={"success" : "ok"})
	
routers = [app]
