from fastapi import Request
from fastapi.responses import JSONResponse


def get_token(request: Request):
    token = request.cookies.get("access_token")

    if not token:
        return JSONResponse(
            status_code=401, content={
                "user_not_valid": "User not logged in"})

    return token


def get_users(token):
    pass
