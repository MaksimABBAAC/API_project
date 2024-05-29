from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import user
from src.comment.models import comments
from src.comment.schemas import CommentCreate
from src.database import get_async_session

router = APIRouter(
    prefix="/comment",
    tags=["Comment"],
)


@router.get("/")
async def get_comment_by_id_coin(id_coin: int, session: AsyncSession = Depends(get_async_session)):
    query = select(comments).where(comments.c.id_coin == id_coin)
    result = await session.execute(query)
    return result.mappings().all()


@router.post("/")
async def add_comment_id_coin(new_comment: CommentCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(comments).values(**new_comment.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/user")
async def get_user_by_id(id_user: int, session: AsyncSession = Depends(get_async_session)):
    query = select(user.c.username, user.c.email).where(user.c.id == id_user)
    result = await session.execute(query)
    return result.mappings().all()
