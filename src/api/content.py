from fastapi import APIRouter

from src.api.dependencies import UserRoleDep
from src.exceptions import AdminOnlyAccessHTTPException

router = APIRouter(prefix="/auth", tags=["Авторизация и аутентификация"])

@router.get("/admin-content")
async def get_admin_content(role: UserRoleDep):
    if role != "admin":
        raise AdminOnlyAccessHTTPException
    return {"content": "Только для админов"}

@router.get("/user-content")
async def get_user_content(role: UserRoleDep):
    if role != "user":
        raise AdminOnlyAccessHTTPException
    return {"content": "Только для пользователей"}