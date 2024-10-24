from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.database import Base

if TYPE_CHECKING:
    from bot.database import Account, AccountSlot


class Profile(Base):
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    telegram_username: Mapped[str | None] = mapped_column(String, nullable=True)
    is_start: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    account_slots: Mapped[list["AccountSlot"]] = relationship(
        back_populates="profile", uselist=True, lazy="selectin"
    )
    accounts: Mapped[list["Account"]] = relationship(
        back_populates="profile", uselist=True, lazy="selectin"
    )