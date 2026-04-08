# ruff: noqa F401
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean

from src.database import Base


class UsersOrm(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    nick_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(200), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(200))
    role: Mapped[str] = mapped_column(String(100), default="guest")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
