from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, ForeignKey, String, Uuid, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.database import Base

if TYPE_CHECKING:
    from bot.database import AccountSlot


class Account(Base):
    account_slot_id: Mapped[int] = mapped_column(ForeignKey("account_slot.id"), nullable=True)
    avito_user_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    avito_client_id: Mapped[str] = mapped_column(String, nullable=False)
    avito_client_secret: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    uuid: Mapped[Uuid] = mapped_column(Uuid, nullable=False, server_default=text("gen_random_uuid()"))
    status: Mapped[bool] = mapped_column(nullable=False, default=False)
    account_slot: Mapped["AccountSlot"] = relationship(
        back_populates="account", uselist=False, lazy="selectin"
    )