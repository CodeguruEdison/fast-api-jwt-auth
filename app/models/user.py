from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from app.config.database import Base
from sqlalchemy.orm import Mapped,mapped_column

class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(String(150))
    email:Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password:Mapped[str] = mapped_column(String(100))
    is_active:Mapped[bool] = mapped_column(Boolean, default=False)
    verified_at:Mapped[datetime] = mapped_column(DateTime, nullable=True, default=None)
    updated_at:Mapped[datetime] = mapped_column(DateTime, nullable=True, default=None, onupdate=datetime.now)
    created_at:Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())