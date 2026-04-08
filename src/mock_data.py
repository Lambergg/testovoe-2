import asyncio
from passlib.context import CryptContext
from pathlib import Path
import sys
from sqlalchemy import text
import logging

sys.path.append(str(Path(__file__).parent.parent))

from src.database import async_session_maker
from src.models.users import UsersOrm

logging.basicConfig(level=logging.INFO)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

AsyncSessionLocal = async_session_maker


async def seed_data():
    async with AsyncSessionLocal() as session:
        async with session.begin():
            await session.execute(text("DELETE FROM users"))

            users = [
                UsersOrm(
                    name="Админ",
                    nick_name="Админович",
                    email="admin@example.com",
                    hashed_password=pwd_context.hash("admin1234"),
                    role="admin",
                ),
                UsersOrm(
                    name="Менеджер",
                    nick_name="Менеджеров",
                    email="manager@example.com",
                    hashed_password=pwd_context.hash("manager1234"),
                    role="user",
                ),
                UsersOrm(
                    name="Обычный",
                    nick_name="Пользователь",
                    email="user@example.com",
                    hashed_password=pwd_context.hash("user1234"),
                    role="user",
                ),
                UsersOrm(
                    name="Гость",
                    nick_name="Обычный",
                    email="guest@example.com",
                    hashed_password=pwd_context.hash("guest1234"),
                    role="guest",
                ),
            ]

            session.add_all(users)

        await session.commit()
        logging.info("Тестовые данные успешно загружены!")


if __name__ == "__main__":
    asyncio.run(seed_data())
