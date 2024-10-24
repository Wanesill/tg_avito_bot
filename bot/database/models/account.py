from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Boolean, ForeignKey, String, text, Uuid, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.database import Base

if TYPE_CHECKING:
    from bot.database import AccountSlot, Profile


class Account(Base):
    profile_id: Mapped[int] = mapped_column(ForeignKey("profile.id"), nullable=False)
    account_slot_id: Mapped[int] = mapped_column(
        ForeignKey("account_slot.id", ondelete='SET NULL'), nullable=True
    )
    account_uuid: Mapped[UUID] = mapped_column(
        Uuid, server_default=text("gen_random_uuid()")
    )
    avito_user_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    avito_client_id: Mapped[str] = mapped_column(String, nullable=False)
    avito_client_secret: Mapped[str] = mapped_column(String, nullable=False)
    avito_token: Mapped[str] = mapped_column(String, nullable=False)
    account_name: Mapped[str] = mapped_column(String, nullable=False)
    account_status: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    profile: Mapped["Profile"] = relationship(
        back_populates="accounts", uselist=False, lazy="joined"
    )
    account_slot: Mapped["AccountSlot"] = relationship(
        back_populates="account", uselist=False, lazy="selectin"
    )
