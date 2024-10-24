from datetime import datetime, timedelta, UTC
from typing import Any, Optional

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert as upsert
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database.models import AccountSlot, Profile


async def test_connection(session: AsyncSession) -> Any:
    return await session.scalar(select(1))


async def upsert_user(
    session: AsyncSession, telegram_id: int, telegram_username: Optional[str]
) -> None:
    stmt = upsert(Profile).values(
        {"telegram_id": telegram_id, "telegram_username": telegram_username}
    )

    stmt = stmt.on_conflict_do_update(
        index_elements=["telegram_id"],
        set_=dict(telegram_username=telegram_username),
    )

    await session.execute(stmt)
    await session.commit()


async def get_profile(
    session: AsyncSession,
    telegram_id: int,
) -> Profile:
    stmt = select(Profile).where(Profile.telegram_id == telegram_id)
    result = await session.execute(stmt)
    return result.unique().scalar_one()


async def insert_account_slots(
    session: AsyncSession,
    profile: Profile,
    count: int,
) -> None:
    subscription_start = datetime.now(UTC)
    days_subscription = 3 if profile.is_start else 30
    subscription_end = subscription_start + timedelta(days=days_subscription)

    for _ in range(count):
        account_slot = AccountSlot(
            profile=profile,
            subscription_start=subscription_start,
            subscription_end=subscription_end,
        )
        session.add(account_slot)

    await session.commit()
