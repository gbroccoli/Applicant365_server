from fastapi import APIRouter, requests
from fastapi.security import OAuth2AuthorizationCodeBearer

app = APIRouter(
	tags=["Auth"],
	prefix="/auth"
)

@app.get("/login")
async def login():
	pass

routers = [app]