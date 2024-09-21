from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

from bot.database import Base

if TYPE_CHECKING:
    from bot.database import Profile


class AccountSlot(Base):
    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return "account_slot"

    profile_id: Mapped[int] = mapped_column(ForeignKey("profile.id"), nullable=False)
    subscription_time: Mapped[int] = mapped_column(DateTime(), nullable=False)
    profile: Mapped["Profile"] = relationship(
        back_populates="account_slots", uselist=False, lazy="joined"
    )
