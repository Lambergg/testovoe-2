from fastapi import APIRouter, status

from src.init import redis_manager_auth

router = APIRouter(prefix="/health", tags=["Health"])


@router.post(
    "/redis_set",
    status_code=status.HTTP_201_CREATED,
    summary="Установка значений",
    description="<h1>Проверка установки данных в Redis, устанавливает ключ B со значением 3421</h1>",
)
async def redis_set():
    key1 = "B"
    value1 = "3421"

    await redis_manager_auth.set(key1, value1)
    return status.HTTP_201_CREATED


@router.get("/get_redis", summary="Получение значений из редиса")
async def get_data_from_redis():
    value_db0 = await redis_manager_auth.get("B")
    return {"value_db0": value_db0}
