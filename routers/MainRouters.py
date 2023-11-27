from fastapi import APIRouter

router = APIRouter(
    tags=['Main']
)


@router.get("/hello", include_in_schema=False)
async def index():
    return {"pease": "hello"}

routers = [router]
