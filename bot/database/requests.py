from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert as upsert
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database.models import AccountSlot, Profile


async def test_connection(session: AsyncSession):
    stmt = select(1)
    return await session.scalar(stmt)


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
    stmt = select(Profile).where(telegram_id == Profile.telegram_id)
    result = await session.execute(stmt)
    return result.unique().scalar_one()


async def insert_account_slots(
    session: AsyncSession,
    profile: Profile,
    count: int,
) -> None:
    subscription_time = (
        datetime.utcnow() - timedelta(days=27)
        if profile.is_start
        else datetime.utcnow()
    )

    for _ in range(count):
        account_slot = AccountSlot(profile=profile, subscription_time=subscription_time)
        session.add(account_slot)

    await session.commit()
