from fastapi import APIRouter

from crud import users
from schemas.users import Customer, Employee

router = APIRouter()


@router.post('/')
async def create_user(user: Employee | Customer):
    return await users.create(user)


@router.get('/')
async def get_users():
    return await users.get()


@router.get('/{user_id}/')
async def get_user(user_id: int):
    return await users.get(user_id)


@router.delete('/{user_id}/')
async def delete_user(user_id: int):
    await users.delete(user_id)
