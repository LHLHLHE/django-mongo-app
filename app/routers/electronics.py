from fastapi import APIRouter

from crud import electronics
from schemas.electronics import Electronic

router = APIRouter()


@router.post('/')
async def create_user(electronic: Electronic):
    return await electronics.create(electronic)


@router.get('/')
async def get_users():
    return await electronics.get()


@router.get('/{electronics_id}/')
async def get_user(electronics_id: int):
    return await electronics.get(electronics_id)


@router.delete('/{electronics_id}/')
async def delete_user(electronics_id: int):
    await electronics.delete(electronics_id)
