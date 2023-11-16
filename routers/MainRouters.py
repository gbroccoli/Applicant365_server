from fastapi import APIRouter

router = APIRouter(
    tags=['Main']
)

@router.get("/hello")
async def index():
    return {}

routers = [router]