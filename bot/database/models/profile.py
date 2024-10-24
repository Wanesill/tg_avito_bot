from sqlalchemy import BigInteger, Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from bot.database import Base


class Profile(Base):
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    telegram_username: Mapped[str | None] = mapped_column(String, nullable=True)
    is_start: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
