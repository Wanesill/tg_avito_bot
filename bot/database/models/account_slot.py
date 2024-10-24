from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

from bot.database import Base

if TYPE_CHECKING:
    from bot.database import Account, Profile


class AccountSlot(Base):
    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return "account_slot"

    profile_id: Mapped[int] = mapped_column(ForeignKey("profile.id"), nullable=False)
    subscription_start: Mapped[int] = mapped_column(DateTime(), nullable=False)
    subscription_end: Mapped[int] = mapped_column(DateTime(), nullable=False)
    profile: Mapped["Profile"] = relationship(
        back_populates="account_slots", uselist=False, lazy="joined"
    )
    account: Mapped["Account"] = relationship(
        back_populates="account_slot", uselist=False, lazy="selectin"
    )
