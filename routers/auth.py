from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2AuthorizationCodeBearer
from core.config.hashing import PasswordManager
from core.config.datebase import async_session_maker
from pydantic import BaseModel
from typing import Optional
import logging
from core.features.datadase import DatabaseCRUD
from core.features.password import ValidationPassword

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

@app.post("/register")
async def register(nominee: Nominee):

	result = await DatabaseCRUD.selectDB(query="SELECT login FROM users WHERE login = :login", data={"login" : nominee.login})
	if result:
		return JSONResponse(status_code=400, content={"error" : "Данный пользователь уже существует" })

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
